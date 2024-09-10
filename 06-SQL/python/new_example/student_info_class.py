import sqlite3
from tabulate import tabulate

# Instead of function based this is now class based
# All data will be first "saved" to the class
# Then there will be an option to add to the data to the db

class Student:
    def __init__(self):
        self.queries = []
        self.query_descriptions = []


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

    def create_table(self):
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
        
        result = self.query_db(query)
        return result
        
    def insert_student(self):
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

        result = self.query_db(query)
        return result

    def view_all_students(self):
        query = "SELECT * FROM student;"

        result = self.query_db(query)
        return result

    def view_student(self, id):
        query = f"SELECT * FROM student WHERE id={id};"

        result = self.query_db(query)
        return result

    def delete_student(self, id):
        query = f"DELETE FROM student WHERE id={id} RETUNING *"
        result = self.query_db(query)
        return result


    def update_student(self, id):
        student = self.view_student(id)[0]
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

        result = self.query_db(query)
        return result

    def main(self):
        self.create_table()
        while True:
            print("Welcome to student data getter")
            print("What would you like to do?")
            choice = input("""
            1. Get all student data
            2. insert student data
            3. Get specific student data
            4. Delete a student
            5. Update a student
            6. View staged changes
            7. Execute changes
            8. Exit
        """)
            
            if choice == "1":
                student_list = self.view_all_students()
                print(tabulate(student_list, headers=["id", "first_name", "last_name", "birthdate", "tz", "favorite_color"]))
                print('\n')
            elif choice == "2":
                self.insert_student()
                print("data inserted successfully")
            elif choice == "3":
                stud_id = input("Choose student id: ")
                student = self.view_student(stud_id)
                print(tabulate(student, headers=["id", "first_name", "last_name", "birthdate", "tz", "favorite_color"]))
            elif choice == "4":
                stud_id = input("Choose student id: ")
                print("Are you sure you want to delete this student?")
                print(self.view_student(stud_id))
                yes_no = input("y/N")
                if yes_no == "y" or "yes":
                    self.delete_student(stud_id)
            elif choice == "5":
                stud_id = input("Choose student id: ")
                self.update_student(stud_id)
                student = self.view_student(stud_id)
                print(tabulate(student, headers=["id", "first_name", "last_name", "birthdate", "tz", "favorite_color"]))
            else:
                break

            input()