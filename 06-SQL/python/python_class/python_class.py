import mysql.connector

class Database:
  def __init__(self, host, user, passwd, database):
      self.mydb = mysql.connector.connect(
        host=host,
        user=user,
        passwd=passwd,
        database=database
      )
      self.mycursor = self.mydb.cursor()

  def dump_to_file(self, filename):
      try:
        self.mycursor.execute("SHOW TABLES")
        tables = self.mycursor.fetchall()
        
        with open(filename, 'w') as file:
          for table in tables:
              table_name = table[0]
              # Dump the structure of the table
              self.mycursor.execute(f"SHOW CREATE TABLE {table_name}")
              create_table_sql = self.mycursor.fetchone()[1] + ";\n"
              file.write(f"-- Dumping structure for table {table_name}\n")
              file.write(create_table_sql)

              # Dump the data of the table
              self.mycursor.execute(f"SELECT * FROM {table_name}")
              rows = self.mycursor.fetchall()
              if rows:
                file.write(f"-- Dumping data for table {table_name}\n")
                for row in rows:
                  values = ', '.join([f"'{str(v)}'" if v is not None else 'NULL' for v in row])
                  file.write(f"INSERT INTO {table_name} VALUES ({values});\n")
        print(f"Database dumped into {filename} successfully.")
      except Exception as e:
        print(f"Error while dumping database: {e}")
  
  def restore_from_file(self, filename):
      try:
        with open(filename, 'r') as file:
          sql_commands = file.read().split(';\n')
          for command in sql_commands:
              if command.strip():
                self.mycursor.execute(command)
                self.mydb.commit()
        print(f"Database restored from {filename} successfully.")
      except Exception as e:
        print(f"Error while restoring database: {e}")


db = Database(host="localhost", user="yourusername", passwd="yourpassword", database="mydatabase")

db.dump_to_file('dump.sql')

new_db = Database(host="localhost", user="yourusername", passwd="yourpassword", database="newdatabase")
new_db.restore_from_file('dump.sql')
