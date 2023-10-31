import sqlite3


def db_get_single(sql, pk) -> sqlite3.Row:
    """Retrieve a single row from a database table

    Args:
        sql (string): SQL string
        pk (int): Primary of item to retrieve

    Returns:
        sqlite3.Row: The row object representing the retrieved row
    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute(sql, (pk,))
        return db_cursor.fetchone()


def db_get_all(sql) -> list:
    """Retrieve all rows from a database table

    Args:
        sql (string): SQL string

    Returns:
        list: List of sqlite3.Row objects
    """
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute(sql)
        return db_cursor.fetchall()
