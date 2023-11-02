import json
from sqlFetch import db_get_single, db_get_all, db_create, db_delete
from nss_handler import status


class OrderView:
    def get(self, handler, pk):
        url = handler.parse_url(handler.path)
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
            query_results_dict = dict(query_results)

            if "_expand" in url["query_params"]:
                if "metal" in url["query_params"]["_expand"]:
                    sql = """
                        SELECT
                        m.id,
                        m.metal,
                        m.price
                        FROM Metals m
                        WHERE m.id = ?"""
                    metal_query_results = db_get_single(
                        sql, query_results_dict["metalId"]
                    )
                    metal_query_results_dict = dict(metal_query_results)
                    query_results_dict["metal"] = metal_query_results_dict
                if "size" in url["query_params"]["_expand"]:
                    sql = """
                        SELECT
                        s.id,
                        s.caret,
                        s.price
                        FROM Sizes s
                        WHERE s.id = ?"""
                    size_query_results = db_get_single(
                        sql, query_results_dict["sizeId"]
                    )
                    size_query_results_dict = dict(size_query_results)
                    query_results_dict["size"] = size_query_results_dict
                if "style" in url["query_params"]["_expand"]:
                    sql = """
                        SELECT
                        s.id,
                        s.style,
                        s.price
                        FROM Styles s
                        WHERE s.id = ?"""
                    style_query_results = db_get_single(
                        sql, query_results_dict["styleId"]
                    )
                    style_query_results_dict = dict(style_query_results)
                    query_results_dict["style"] = style_query_results_dict
            order_json_object = json.dumps(query_results_dict)
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
            if "_expand" in url["query_params"]:
                orders_list = []
                for order in orders:
                    order_id = order["id"]
                    if order_id not in orders_list:
                        if "metal" in url["query_params"]["_expand"]:
                            sql = """
                                    SELECT
                                    m.id,
                                    m.metal,
                                    m.price
                                    FROM Metals m
                                    WHERE m.id = ?"""
                            metal_query_results = db_get_single(sql, order["metalId"])
                            metal_query_results_dict = dict(metal_query_results)
                            order["metal"] = metal_query_results_dict
                        if "size" in url["query_params"]["_expand"]:
                            sql = """
                                    SELECT
                                    s.id,
                                    s.caret,
                                    s.price
                                    FROM Sizes s
                                    WHERE s.id = ?"""
                            size_query_results = db_get_single(sql, order["sizeId"])
                            size_query_results_dict = dict(size_query_results)
                            order["size"] = size_query_results_dict
                        if "style" in url["query_params"]["_expand"]:
                            sql = """
                                    SELECT
                                    s.id,
                                    s.style,
                                    s.price
                                    FROM Styles s
                                    WHERE s.id = ?"""
                            style_query_results = db_get_single(sql, order["styleId"])
                            style_query_results_dict = dict(style_query_results)
                            order["style"] = style_query_results_dict
                        orders_list.append(order)
                        orders_json_array = json.dumps(orders_list)
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
