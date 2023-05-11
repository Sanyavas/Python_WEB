from connection import create_connection


def create_table(conn, sql_execute):
    c = conn.cursor()
    c.execute(sql_execute)
    c.close()


if __name__ == '__main__':
    sql_e = """
    DROP TABLE IF EXISTS groups;
    CREATE TABLE IF NOT EXISTS groups (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100)
    );

    DROP TABLE IF EXISTS teachers;
    CREATE TABLE IF NOT EXISTS teachers (
        id SERIAL PRIMARY KEY,
        fullname VARCHAR(100),
        phone VARCHAR(100),
        address VARCHAR(100)
    );

    DROP TABLE IF EXISTS students;
    CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        fullname VARCHAR(100),
        email VARCHAR(100),
        phone VARCHAR(100),
        age VARCHAR(100),
        group_id INTEGER,
        FOREIGN KEY (group_id) REFERENCES groups(id)
    );

    DROP TABLE IF EXISTS disciplines;
    CREATE TABLE IF NOT EXISTS disciplines (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) UNIQUE,
        teacher_id INTEGER,
        FOREIGN KEY (teacher_id) REFERENCES teachers(id)
    );

    DROP TABLE IF EXISTS grades;
    CREATE TABLE IF NOT EXISTS grades (
        id SERIAL PRIMARY KEY,
        student_id INTEGER,
        discipline_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES students(id),
        FOREIGN KEY (discipline_id) REFERENCES disciplines(id),
        grade INTEGER,
        date_of DATE
    );
    """

    with create_connection() as conn:
        create_table(conn, sql_e)

        print(f'[INFO] Create tables in postgreSQL - OK!')
