import psycopg2

def get_db_connection():
    return psycopg2.connect(
        dbname="finance_db",
        user="aaron",
        password="",
        host="localhost",
        port="5432"
    )


class MenuManager:
    def get_by_name():
        get_db_connection()

    def save():
        pass

    def delete():
        pass

    def update():
        pass

