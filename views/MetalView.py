class MetalView:
    def get(self, handler, pk):
        if pk != 0:
            sql = """
                SELECT 
                m.id,
                m.metal,
                m.price
                FROM Metals m
                """
            query_results = db_get_single(
                sql,
            )
