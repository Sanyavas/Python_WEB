import sys
from prettytable import PrettyTable

from connection import create_connection
from aux_functions import help_message


def query_sql(file):
    with open(file) as f:
        sql = f.read()

    with create_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()


if __name__ == '__main__':
    print(help_message())
    x = PrettyTable()
    while True:
        try:
            task = int(input("Виберіть номер запиту: "))
            if task == 0:
                sys.exit()
            if task == 33:
                print(help_message())
                continue
            result = query_sql(f"requests/request_{task}.sql")
            for i in result:
                x.field_names = [str(num) for num in range(1, len(i) + 1)]
                x.align = "l"
                x.add_row(i)
            print(x)
            x = PrettyTable()
        except TypeError as err:
            print(f'[ERROR] {err}')
        except FileNotFoundError as err:
            print(f'[ERROR] {err}')
        except ValueError as err:
            print(f'[ERROR] {err}')

