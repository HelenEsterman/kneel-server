import json
from sqlFetch import db_get_single, db_get_all
from nss_handler import status


class StyleView:
    def get(self, handler, pk):
        if pk != 0:
            sql = """
                SELECT 
                s.id,
                s.style,
                s.price
                FROM Styles s
                WHERE s.id = ?
                """
            query_results = db_get_single(sql, pk)
            style_json_object = json.dumps(dict(query_results))
            return handler.response(style_json_object, status.HTTP_200_SUCCESS.value)
        else:
            sql = """
                SELECT 
                s.id,
                s.style,
                s.price
                FROM Styles s
                """
            query_results = db_get_all(sql)
            styles = [dict(row) for row in query_results]
            styles_json_array = json.dumps(styles)
            return handler.response(styles_json_array, status.HTTP_200_SUCCESS.value)

    def delete_put_post(self, handler):
        return handler.response(
            "Functionality is not supported", status.HTTP_405_UNSUPPORTED_METHOD.value
        )
