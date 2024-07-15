import psycopg2

try:
    conn = psycopg2.connect(
        dbname="testdb",
        user="sanvi",
        password="1234",
        host="localhost",
        port="5432"
    )
    print("Connection successful")
    conn.close()
except Exception as e:
    print(f"An error occurred: {e}")
