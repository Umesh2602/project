import psycopg2

def connect():
    conn = None
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="testdb",
            user="sanvi",
            password="1234"
        )
        print("Connected successful")
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

def create_schema(conn):
    try:
        cursor = conn.cursor()
        create_schema_query = "create schema if not exists student_management"
        cursor.execute(create_schema_query)
        conn.commit()
        print("Schema 'student_management' created successfully")
    except psycopg2.Error as e:
        print(f"Error creating schema: {e}")

def create_table(conn):
    try:
        cursor = conn.cursor()
        create_table_query = """
        create table if not exists student_management.students(
            student_id serial primary key,
            student_name varchar(100),
            age int,
            grade varchar(10)
        )
        """
        cursor.execute(create_table_query)
        conn.commit()
        print("Table 'students' created successfully")
    except psycopg2.Error as e:
        print(f"Error creating table: {e}")

def insert_data(conn):
    try:
        cursor = conn.cursor()
        insert_query = """
        insert into student_management.students (student_name, age, grade)
        values 
        ('Umesh', 20, 'A'),
        ('Rahul', 21, 'B'),
        ('Abi', 19, 'C'),
        ('Rithik', 20, 'A')
        """
        cursor.execute(insert_query)
        conn.commit()
        print("Data inserted successfully")
    except psycopg2.Error as e:
        print(f"Error inserting data: {e}")

def delete_data(conn, student_id):
    try:
        cursor = conn.cursor()
        delete_query = """
        delete from student_management.students
        where student_id = %s
        """
        cursor.execute(delete_query, (student_id,))
        conn.commit()
        print(f"Data with student_id {student_id} deleted successfully")
    except psycopg2.Error as e:
        print(f"Error deleting data: {e}")

def select_data(conn):
    try:
        cursor = conn.cursor()
        select_query = "select * from student_management.students"
        cursor.execute(select_query)
        students = cursor.fetchall()
        for student in students:
            print(f"Student ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
    except psycopg2.Error as e:
        print(f"Error selecting data: {e}")

def main():
    conn = connect()
    if conn is None:
        return

    create_schema(conn)
    create_table(conn)
    insert_data(conn)
    select_data(conn)
    delete_data(conn, 4)
    select_data(conn)

    conn.close()
    print("PostgreSQL connection is closed")

if __name__ == "__main__":
    main()
