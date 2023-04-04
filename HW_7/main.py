import argparse

from prettytable import PrettyTable

from my_select import main as query_main
from database.repository import create_data, read_data, update_data, delete_data
from database.models import Teacher, Student, Discipline, Group, Grade

parser = argparse.ArgumentParser(description="CLI")
parser.add_argument("--action", "-a", help="Command: create, read, update, delete")
parser.add_argument("--model", "-m", help="Teacher, Student, Group, Grade, Discipline")
parser.add_argument("--query", "-q")
parser.add_argument("--name", "-n")
parser.add_argument("--phone", "-p")
parser.add_argument("--address", "-ad")
parser.add_argument("--email", "-e")
parser.add_argument("-id")
parser.add_argument("--discipline_id", "-did")
parser.add_argument("--student_id", "-sid")
parser.add_argument("--date_of", "-dof")
parser.add_argument("--grade_id", "-gid")

arguments = parser.parse_args()
my_arg = vars(arguments)

action = my_arg.get('action')
model = my_arg.get('model')
query = my_arg.get('query')


# _id = my_arg.get('id')
# name = my_arg.get('name')
# phone = my_arg.get('phone')
# address = my_arg.get('address')
# email = my_arg.get('email')


def main():
    try:
        my_model = None
        match model:
            case 'student':
                my_model = Student
            case 'teacher':
                my_model = Teacher
            case 'discipline':
                my_model = Discipline
            case 'group':
                my_model = Group
            case 'grade':
                my_model = Grade

        match action:
            case 'create':
                data = create_data(my_model, my_arg)
                print(data)
            case 'read':
                a = read_data(my_model)
                x = PrettyTable()
                for i in a:
                    x.add_row(i)
                print(x)
            case 'update':
                upd = update_data(my_model, my_arg)
                print(my_arg)
                print(f'Update: {model}_id_{upd.id}')
            case 'delete':
                dd = delete_data(my_model, my_arg)
                print(f"Remove {dd.id}")

        if query:
            query_main(query)

    except ValueError as err:
        print(f'ValueError {err}')
    except TypeError as err:
        print(f'TypeError {err}')
    except AttributeError as err:
        print(f'AttributeError {err}')


if __name__ == '__main__':
    main()
