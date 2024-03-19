# COMP 3005A3 Q1

### Install
1. Create a database through pgadmin and paste in the db.sql contents into the Query Tool.

2. Run the following command:
```
pip install psycopg2
```

3. Change the constant `DB_NAME` to the name of the database created in step 1.

4. Run the following command:
```
python main.py
```

### Function Explanation
`getAllStudents()`: Selects all from the `students` table and returns the contents to the REPL to be displayed.

`addStudent(first_name, last_name, email, enrollment_date)`: Adds a new student to the `students` table based on the given parameters and returns True/False status on the operation to the REPL to be displayed.

`updateStudentEmail(student_id, new_email)`: Updates a student email based on the provided `student_id` and returns True/False on the operation to the REPL to be displayed.

`deleteStudent(student_id)`: Deletes a record based on the `student_id` and returns True/False on the operation to the REPL to be displayed.

### Error Handling
Error handling is done in two different stages: user-input level, and at the query level.

At the user-input level, it checks whether the user supplied a valid operation, and whether they supplied the correct amount of operands. If there is an error, since this is a REPL, it will print an error message and continue in the `while True` loop.

At the query level, it catches any fatal errors that may be caused, and as such calls `exit()`.

### Video
https://youtu.be/3PFN7g5kg-o
