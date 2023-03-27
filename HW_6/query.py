import sys
from prettytable import from_db_cursor

from connection import create_connection
from aux_functions import help_message


def query_sql(file):
    with open(file) as f:
        sql = f.read()

    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        # return cursor.fetchall()
        return from_db_cursor(cursor)


def main():
    print(help_message())
    while True:
        try:
            task = int(input(f"\nВиберіть номер запиту: "))
            if task == 0:
                sys.exit()
            if task == 33:
                print(help_message())
                continue
            result = query_sql(f"requests/request_{task}.sql")
            print(result)

        except TypeError as err:
            print(f'[ERROR] {err}')
        except FileNotFoundError as err:
            print(f'[ERROR] {err}')
        except ValueError as err:
            print(f'[ERROR] {err}')


if __name__ == '__main__':
    main()

