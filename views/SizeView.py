import json
from sqlFetch import db_get_single, db_get_all
from nss_handler import status


class SizeView:
    def get(self, handler, pk):
        if pk != 0:
            sql = """
                SELECT 
                s.id,
                s.caret,
                s.price
                FROM Sizes s
                WHERE s.id = ?
                """
            query_results = db_get_single(sql, pk)
            size_json_object = json.dumps(dict(query_results))
            return handler.response(size_json_object, status.HTTP_200_SUCCESS.value)
        else:
            sql = """
                SELECT 
                s.id,
                s.caret,
                s.price
                FROM Sizes s
                """
            query_results = db_get_all(sql)
            sizes = [dict(row) for row in query_results]
            sizes_json_array = json.dumps(sizes)
            return handler.response(sizes_json_array, status.HTTP_200_SUCCESS.value)

    def delete(self, handler, pk):
        return handler.response(
            "Functionality is not supported", status.HTTP_405_UNSUPPORTED_METHOD.value
        )
