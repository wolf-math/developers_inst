import psycopg2
from psycopg2 import sql
import requests
import json


def get_db_connection():
    return psycopg2.connect(
        dbname="finance_db",
        user="aaron",
        password="",
        host="localhost",
        port="5432"
    )


def create_db():
    try:
        conn = get_db_connection()
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(sql.SQL(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = {'finance_db'}"))
        exists = cursor.fetchone()
        if not exists:
            cursor.execute(sql.SQL('CREATE DATABASE finance_db'))
            print("Database 'finance_db' created successfully.")
        else:
            print("Database 'finance_db' already exists.")
        conn.close()
    except Exception as e:
        print(f"Error creating database: {e}")
        return

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id SERIAL PRIMARY KEY,
                amount REAL,
                category VARCHAR(255),
                description TEXT,
                date DATE,
                currency VARCHAR(10)
            )
        ''')
        conn.commit()
        conn.close()
        print("Table 'transactions' created successfully (if it didn't already exist).")
    except Exception as e:
        print(f"Error connecting to 'finance_db' or creating the table: {e}")


def add_transaction(amount, category, description, date, currency):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO transactions (amount, category, description, date, currency) VALUES ({amount}, '{category}', '{description}', '{date}', '{currency}')")
    conn.commit()
    conn.close()


def convert_currency(amount, from_currency, to_currency):
    api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(api_url)
    rates = response.json()["rates"]
    converted_amount = amount * rates[to_currency]
    return converted_amount


def view_transactions(filter_by=None, filter_value=None):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM transactions"
    if filter_by and filter_value:
        query += f" WHERE {filter_by} = %s"
        cursor.execute(query, (filter_value,))
    else:
        cursor.execute(query)

    transactions = cursor.fetchall()
    conn.close()

    for transaction in transactions:
        print(transaction)



def export_to_json():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()
    conn.close()

    transactions = json.dumps(transactions)

    print(transactions)

    # with open('transactions.json', 'w') as json_file:
    #     json.dump(transactions, json_file)