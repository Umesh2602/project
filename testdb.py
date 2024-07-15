import psycopg2

try:
    connection = psycopg2.connect(host="localhost",
                                  database="testdb",
                                  user="sanvi",
                                  password="1234")
    print("Connection successful")

    cursor = connection.cursor()

    create_schema_query = "create schema student_management"
    cursor.execute(create_schema_query)
    print("Schema 'student_management' created successfully")

    create_table_query = """
    create table student_management.students( student_id serial primary key,student_name varchar(255),age int,grade varchar(10))
    """
    cursor.execute(create_table_query)
    print("Table 'students' created successfully")

    insert_query = """
    insert into student_management.students (student_name, age, grade)
    values 
    ('Umesh', 20, 'A'),
    ('Rahul', 21, 'B'),
    ('Abi', 19, 'C'),
    ('Rithik,20,'A')

    """
    cursor.execute(insert_query)
    print("Data inserted successfully")

    select_query = "select * from student_management.students"
    cursor.execute(select_query)
    students = cursor.fetchall()
    for student in students:
        print(f"Student ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Grade: {student[3]}")
        
    connection.commit()

except psycopg2.Error as e:
    print("Error while connecting to PostgreSQL:", e)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
