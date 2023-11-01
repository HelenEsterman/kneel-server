import json
from sqlFetch import db_get_single, db_get_all, db_create, db_delete
from nss_handler import status


class OrderView:
    def get(self, handler, pk):
        if pk != 0:
            sql = """
                SELECT 
                o.id,
                o.metalId,
                o.sizeId,
                o.styleId
                FROM `Orders` o
                WHERE o.id = ?
                """
            query_results = db_get_single(sql, pk)
            order_json_object = json.dumps(dict(query_results))
            return handler.response(order_json_object, status.HTTP_200_SUCCESS.value)
        else:
            sql = """
                SELECT 
                o.id,
                o.metalId,
                o.sizeId,
                o.styleId
                FROM `Orders` o
                """
            query_results = db_get_all(sql)
            orders = [dict(row) for row in query_results]
            orders_json_array = json.dumps(orders)
            return handler.response(orders_json_array, status.HTTP_200_SUCCESS.value)

    def put(self, handler):
        return handler.response(
            "Functionality is not supported", status.HTTP_405_UNSUPPORTED_METHOD.value
        )

    def post(self, handler, order_data):
        sql = """
            INSERT INTO `Orders` 
            (metalId, sizeId, styleId) VALUES (?,?,?)"""
        posted_order_id = db_create(
            sql, (order_data["metalId"], order_data["sizeId"], order_data["styleId"])
        )
        order = {
            "id": posted_order_id,
            "metalId": order_data["metalId"],
            "sizeId": order_data["sizeId"],
            "styleId": order_data["styleId"],
        }
        posted_order = json.dumps(order)

        if posted_order_id:
            return handler.response(posted_order, status.HTTP_201_SUCCESS_CREATED.value)
        else:
            return handler.response(
                "Problem encountered when trying to carry out post request",
                status.HTTP_500_SERVER_ERROR.value,
            )

    def delete(self, handler, pk):
        number_of_rows_deleted = db_delete("DELETE FROM `Orders` WHERE id = ?", pk)

        if number_of_rows_deleted:
            return handler.response(
                "",
                status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value,
            )
        else:
            return handler.response(
                "Problem encountered when trying to carry out deletion request",
                status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value,
            )
