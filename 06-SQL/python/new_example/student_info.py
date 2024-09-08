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

# first name
# last name
# birthdate
# tz
# favorite_color

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
    create_student_table = """CREATE TABLE IF NOT EXISTS student (
                id INTEGER PRIMARY KEY, 
                first_name varchar(50) NOT NULL, 
                last_name varchar(50) NOT NULL, 
                birthdate DATE,
                tz int,
                favorite_color varchar(50) NOT NULL     
        );
        """
    
    result = query_db(create_student_table)
    return result
    
def insert_data():
    # student_info = {first_name, last_name, birthdate, tz, favorite_color}
    first_name = input('first name: ')
    last_name = input('last name: ')
    birthdate = input('birthdate: ')
    tz = input('tz: ')
    favorite_color = input('favorite color: ')

    student_info = {
        "first_name": first_name, 
        "last_name": last_name, 
        "birthdate": birthdate, 
        "tz": tz, 
        "favorite_color": favorite_color
        }

    insert_student_data = f"""
        INSERT INTO student (first_name, last_name, birthdate, tz, favorite_color)
        VALUES (
            '{student_info['first_name']}',
            '{student_info['last_name']}',
            '{student_info['birthdate']}',
            {student_info['tz']},
            '{student_info['favorite_color']}'
        );
    """

    result = query_db(insert_student_data)
    return result

def view_all_students():
    view_students = "SELECT * FROM student;"

    result = query_db(view_students)
    return result

def main():
    create_table()
    while True:
        print("Welcome to student data getter")
        print("What would you like to do?")
        choice = input("""
        1. Get all student data
        2. insert student data
        3. exit
    """)
        
        if choice == "1":
            student_list = view_all_students()
            print(tabulate(student_list, headers=["first_name", "last_name", "birthdate", "tz", "favorite_color"]))

        elif choice == "2":
            insert_data()
            print("data inserted successfully")
        else:
            break

        
if __name__ == "__main__":
    main()
