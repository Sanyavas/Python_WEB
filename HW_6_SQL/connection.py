from contextlib import contextmanager

from psycopg2 import connect, Error


@contextmanager
def create_connection():
    conn = None
    try:
        conn = connect(host='localhost', user='postgres', password='567234', database='postgres', port=5432)
        yield conn
        conn.commit()
    except Error as err:
        print(f'[ERROR] Connection  {err}')
        conn.rollback()
    finally:
        if conn:
            conn.close()
