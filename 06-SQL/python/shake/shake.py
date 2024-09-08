import sqlite3
from tabulate import tabulate

def order():
    create_table()
    choice = None
    while choice != "X":
        print("Moti's Fruit Shake Stand with questionable hygiene")
        inv = get_inv()
        print(tabulate(inv, headers=['Fruit', 'Amount']))
        choice = input("What do you want to add to your shake?")
        update_inv(choice)
    else:
        print("Bye")

def update_inv(choice):
    query = f"UPDATE fruit SET quantity=quantity-1 WHERE name = '{choice}';"
    return run_query(query)

def get_inv():
    query = "SELECT name, quantity FROM fruit ORDER BY name ASC;"
    return run_query(query)

def run_query(query):
    connection = sqlite3.connect("shakes.db")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    results = cursor.fetchall()
    connection.close()
    return results

def create_table():
    create_fruit_table = """CREATE TABLE IF NOT EXISTS fruit (
                id INTEGER PRIMARY KEY, 
                name text NOT NULL, 
                quantity smallint
        );
        """
    
    insert_fruit = """
        INSERT INTO fruit (name, quantity)
        VALUES 
        ('banana', 12),
        ('strawberry', 35),
        ('onion', 100),
        ('apple', 24);
"""
    
    try:
        with sqlite3.connect('shakes.db') as conn:
            cursor = conn.cursor()
            cursor.execute(create_fruit_table)
            cursor.execute(insert_fruit)
            conn.commit()
            conn.close()
    except sqlite3.Error as e:
        print(e)

if __name__ == "__main__":
    order()