import json
from sqlFetch import db_get_single, db_get_all
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
