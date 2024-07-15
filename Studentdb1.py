import psycopg2

def connect_to_db():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="testdb",
            user="sanvi",
            password="1234"
        )
        print("Connection successful")
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None

def create_schema(cursor):
    try:
        create_schema_query = "create schema if not exists student_management"
        cursor.execute(create_schema_query)
        print("Schema 'student_management' created successfully")
    except psycopg2.Error as e:
        print(f"Error creating schema: {e}")

def create_table(cursor):
    try:
        create_table_query = """
        create table if not exists student_management.students(
            student_id serial primary key,
            student_name varchar(255),
            age int,
            grade varchar(10),
            course_credit int,
            course_name varchar(255)
        )
        """
        cursor.execute(create_table_query)
        print("Table 'students' created successfully")
    except psycopg2.Error as e:
        print(f"Error creating table: {e}")

def insert_data(cursor):
    try:
        insert_query = """
        insert into student_management.students (student_name, age, grade, course_credit, course_name)
        values 
        ('Umesh', 20, 'A', 3, 'Mathematics'),
        ('Rahul', 21, 'B', 4, 'Science'),
        ('Abi', 19, 'C', 3, 'History'),
        ('Rithik', 20, 'A', 2, 'English')
        """
        cursor.execute(insert_query)
        print("Data inserted successfully")
    except psycopg2.Error as e:
        print(f"Error inserting data: {e}")

def delete_data(cursor, student_id):
    try:
        delete_query = "delete from student_management.students where student_id = %s"
        cursor.execute(delete_query, (student_id,))
        print(f"Data with student_id {student_id} deleted successfully")
    except psycopg2.Error as e:
        print(f"Error deleting data: {e}")

def select_data(cursor):
    try:
        select_query = "select * from student_management.students"
        cursor.execute(select_query)
        students = cursor.fetchall()
        for student in students:
            print(f"Student ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}, Course Credit: {student[4]}, Course Name: {student[5]}")
    except psycopg2.Error as e:
        print(f"Error selecting data: {e}")

def update_data(cursor, student_id, course_credit, course_name):
    try:
        update_query = """
        update student_management.students
        set course_credit = %s, course_name = %s
        where student_id = %s
        """
        cursor.execute(update_query, (course_credit, course_name, student_id))
        print(f"Data for student_id {student_id} updated successfully")
    except psycopg2.Error as e:
        print(f"Error updating data: {e}")

def main():
    conn = connect_to_db()
    if conn is None:
        return

    try:
        cursor = conn.cursor()

        create_schema(cursor)
        create_table(cursor)
        insert_data(cursor)

        select_data(cursor)

        # Update course credit and course name for a specific student (example)
        update_data(cursor, student_id=1, course_credit=4, course_name='Physics')

        select_data(cursor)

        delete_data(cursor, 4)

        select_data(cursor)

        conn.commit()
    except psycopg2.Error as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()
            print("PostgreSQL connection is closed")

if __name__ == "__main__":
    main()
