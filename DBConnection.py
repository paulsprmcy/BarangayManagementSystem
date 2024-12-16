import mysql.connector
from mysql.connector import Error

host = "localhost"
user = "root"
password = ""
database = "barangayDB"

class Connection:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cur = self.connection.cursor()
        except Error as e:
            print(f"Error connecting to database: {e}")
            self.connection = None
            self.cur = None

    def close_connection(self):
        if self.connection:
            self.cur.close()
            self.connection.close()
            print("Connection closed")
    def conn(self):
        return self.connection
    def query(self, q, params=None):
        try:
            if params:
                self.cur.execute(q, params)
            else:
                self.cur.execute(q)
                # self.connection.commit()
            return self.cur.fetchall()
        except Error as e:
            print(f"Error executing query: {e}")
            return None
