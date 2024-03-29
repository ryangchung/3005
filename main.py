import psycopg2

DB_NAME = "student"
USER = "postgres"
PASSWORD = "postgres"
HOST = "localhost"
PORT = "5432"


def connect():
    try:
        connection = psycopg2.connect(
            dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST, port=PORT
        )
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
    return connection


def query(query, return_data, vars=None):
    connection = None
    try:
        connection = connect()
        cursor = connection.cursor()
        cursor.execute(query, vars)
        if return_data:
            data = cursor.fetchall()
            cursor.close()
            return data
        else:
            connection.commit()
            cursor.close()
            return True
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
    finally:
        if connection:
            connection.close()


def getAllStudents():
    return query("SELECT * FROM students", True)


def addStudent(first_name, last_name, email, enrollment_date):
    return query(
        "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
        False,
        (first_name, last_name, email, enrollment_date),
    )


def updateStudentEmail(student_id, email):
    return query("UPDATE students SET email = %s WHERE student_id = %s", False, (email, student_id))


def deleteStudent(student_id):
    return query("DELETE FROM students WHERE student_id = %s", False, (student_id))


while True:
    command = input(
        "Enter a command (command and operand separated by space): "
    ).split()
    if command[0] == "GET":
        print(getAllStudents())
    elif command[0] == "ADD":
        if len(command) == 5:
            print(addStudent(command[1], command[2], command[3], command[4]))
        else:
            print("Error: ADD found! Missing parameters!")
    elif command[0] == "UPDATE_EMAIL":
        if len(command) == 3:
            print(updateStudentEmail(command[1], command[2]))
        else:
            print("Error: UPDATE_EMAIL found! Missing parameters!")
    elif command[0] == "DELETE":
        if len(command) == 2:
            print(deleteStudent(command[1]))
        else:
            print("Error: DELETE found! Missing parameters!")
    elif command[0] == "HELP":
        print("GET: Get all students")
        print("ADD (first_name, last_name, email and enrollment_date): Add a student")
        print("UPDATE_EMAIL (student_id, email) : Update a student's email")
        print("DELETE (student_id): Delete a student")
        print("EXIT: Exit the program\n")
    elif command[0] == "EXIT":
        print("Exiting...")
        break
    else:
        print("Invalid command")
