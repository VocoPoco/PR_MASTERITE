import sqlite3
import os

class User():
    def __init__(self):
        self.connection = sqlite3.connect(os.path.join(os.path.dirname(os.path.realpath(__file__)), "db.sqlite3"))
        self.cur = self.connection.cursor()

    def create_if_not_exists(self):
        """Create db sqlite file if it doesn't exist yet."""
        try:
            self.cur.execute("SELECT * FROM User")
            data_list = self.cur.fetchall() 

        except sqlite3.OperationalError:
            print("Creating!")
            self.cur.execute("""CREATE TABLE User (
                first TEXT,
                last TEXT,
                plus INTEGER,
                minus INTEGER,
                asks INTEGER,
                absence INTEGER,
                studentID INTEGER PRIMARY KEY AUTOINCREMENT
            )""")
            for i, (first, last) in enumerate(self.students):
                self.cur.execute(f"INSERT INTO Class (first, last, plus, minus, asks, absence, studentID) VALUES ('{first}', '{last}', 0, 0, 0, 0, {i+1})")


        self.connection.commit()     

# in progress