# 1. create a virtualenv --> I need to be in the correct directory!!!
# 2. activate the virtualenv
# 3. install deps
# 4. start coding!
#   a. write a function to create a table
#   b. write a function to insert data
#   c. write a function to update data
#   d. write a function to read data (all data/ single student)
#   e. write a function to delete data
#   f. write a "main" function to run these operations

import sqlite3
from tabulate import tabulate

def query_db(query):
    try:
        connection = sqlite3.connect("student.db")
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        results = cursor.fetchall()
        connection.close()
        return results
    except sqlite3.Error as e:
        print(e)

def create_table():
    # I should have made it `student_id` instead of `id`
    query = """CREATE TABLE IF NOT EXISTS student (
                id INTEGER PRIMARY KEY, 
                first_name varchar(50) NOT NULL, 
                last_name varchar(50) NOT NULL, 
                birthdate DATE,
                tz int,
                favorite_color varchar(50) NOT NULL     
        );
        """
    
    query_db(query)
    

def insert_student():
    # student_info = {first_name, last_name, birthdate, tz, favorite_color}
    first_name = input('first name: ')
    last_name = input('last name: ')
    birthdate = input('birthdate: ')
    tz = input('tz: ')
    favorite_color = input('favorite color: ')

    query = f"""
        INSERT INTO student (first_name, last_name, birthdate, tz, favorite_color)
        VALUES (
            '{first_name}',
            '{last_name}',
            '{birthdate}',
            {tz},
            '{favorite_color}'
        );
    """

    query_db(query)


def view_all_students():
    query = "SELECT * FROM student;"

    result = query_db(query)
    return result


def view_student(id):
    query = f"SELECT * FROM student WHERE id={id};"

    result = query_db(query)
    return result


def delete_student(id):
    query = f"DELETE FROM student WHERE id={id}"
    query_db(query)


def update_student(id):
    student = view_student(id)[0]
    first_name = input(f'first name: [default {student[1]}] ')
    last_name = input(f'last name: [default {student[2]}] ')
    birthdate = input(f'birthdate: [default {student[3]}] ')
    tz = input(f'tz: [default {student[4]}] ')
    favorite_color = input(f'favorite color: [default {student[5]}] ')

    query = f"""
        UPDATE student SET
            first_name = '{first_name if first_name != '' else student[1]}',
            last_name = '{last_name if last_name != '' else student[2]}',
            birthdate = '{birthdate if birthdate != '' else student[3]}',
            tz = {tz if tz != '' else student[4]},
            favorite_color = '{favorite_color if favorite_color != '' else student[5]}'
        WHERE id = {id};
    """

    query_db(query)


def main():
    create_table()
    while True:
        print("Welcome to student data getter")
        print("What would you like to do?")
        choice = input("""
        1. Get all student data
        2. insert student data
        3. Get specific student data
        4. Delete a student
        5. Update a student
        6. Exit
    """)
        
        if choice == "1":
            student_list = view_all_students()
            print(tabulate(student_list, headers=["id", "first_name", "last_name", "birthdate", "tz", "favorite_color"]))
            print('\n')
        elif choice == "2":
            insert_student()
            print("data inserted successfully")
        elif choice == "3":
            stud_id = input("Choose student id: ")
            student = view_student(stud_id)
            print(tabulate(student, headers=["id", "first_name", "last_name", "birthdate", "tz", "favorite_color"]))
        elif choice == "4":
            stud_id = input("Choose student id: ")
            print("Are you sure you want to delete this student?")
            print(view_student(stud_id))
            yes_no = input("y/N")
            if yes_no == "y" or "yes":
                delete_student(stud_id)
        elif choice == "5":
            stud_id = input("Choose student id: ")
            update_student(stud_id)
            student = view_student(stud_id)
            print(tabulate(student, headers=["id", "first_name", "last_name", "birthdate", "tz", "favorite_color"]))
        else:
            break
        input()

        
if __name__ == "__main__":
    main()


# Things I changed since class:
# 1. all queries called `query`
# 2. changed insert_data to insert_student
# 3. deleted the student dictionary
# 4. one-line if-statements
