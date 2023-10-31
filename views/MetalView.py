import json
from sqlFetch import db_get_single, db_get_all
from nss_handler import status


class MetalView:
    def get(self, handler, pk):
        if pk != 0:
            sql = """
                SELECT 
                m.id,
                m.metal,
                m.price
                FROM `Metals` m
                WHERE m.id = ?
                """
            query_results = db_get_single(sql, pk)
            metal_json_object = json.dumps(dict(query_results))
            return handler.response(metal_json_object, status.HTTP_200_SUCCESS.value)
        else:
            sql = """
                SELECT 
                m.id,
                m.metal,
                m.price
                FROM `Metals` m
                """
            query_results = db_get_all(sql)
            metals = [dict(row) for row in query_results]
            metals_json_array = json.dumps(metals)
            return handler.response(metals_json_array, status.HTTP_200_SUCCESS.value)
