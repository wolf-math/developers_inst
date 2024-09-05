import sqlite3
import requests
import json

def create_db():
    conn = sqlite3.connect('finance_tracker.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS transactions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  amount REAL,
                  category TEXT,
                  description TEXT,
                  date TEXT,
                  currency TEXT)''')
    conn.commit()
    conn.close()


def add_transaction(amount, category, description, date, currency):
    conn = sqlite3.connect('finance_tracker.db')
    c = conn.cursor()
    c.execute("INSERT INTO transactions (amount, category, description, date, currency) VALUES (?, ?, ?, ?, ?)",
              (amount, category, description, date, currency))
    conn.commit()
    conn.close()


def convert_currency(amount, from_currency, to_currency):
    api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(api_url)
    rates = response.json()["rates"]
    converted_amount = amount * rates[to_currency]
    return converted_amount


def view_transactions(filter_by=None, filter_value=None):
    conn = sqlite3.connect('finance_tracker.db')
    c = conn.cursor()

    query = "SELECT * FROM transactions"
    if filter_by and filter_value:
        query += f" WHERE {filter_by} = ?"
        c.execute(query, (filter_value,))
    else:
        c.execute(query)

    transactions = c.fetchall()
    conn.close()

    for transaction in transactions:
        print(transaction)


def export_to_json():
    conn = sqlite3.connect('finance_tracker.db')
    c = conn.cursor()
    c.execute("SELECT * FROM transactions")
    transactions = c.fetchall()
    conn.close()

    with open('transactions.json', 'w') as json_file:
        json.dump(transactions, json_file)

