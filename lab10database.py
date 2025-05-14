import sqlite3
import threading

class DatabaseOperations:
    def __init__(self):
        self.connection = sqlite3.connect("example.db")
        self.cursor = self.connection.cursor()
    
    def create_table(self):
        try:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)''')
            self.connection.commit()
        except Exception as e:
            print(f"Error: {e}")

    def insert_data(self, name):
        try:
            self.cursor.execute('''INSERT INTO users (name) VALUES (?)''', (name,))
            self.connection.commit()
        except Exception as e:
            print(f"Error: {e}")

    def fetch_data(self):
        try:
            self.cursor.execute('''SELECT * FROM users''')
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Error: {e}")

    def close(self):
        self.connection.close()

class WorkerThread(threading.Thread):
    def __init__(self, db_operations):
        threading.Thread.__init__(self)
        self.db_operations = db_operations
    
    def run(self):
        self.db_operations.insert_data("John Doe")
        self.db_operations.insert_data("Jane Smith")
        print(self.db_operations.fetch_data())

def main():
    db_operations = DatabaseOperations()
    db_operations.create_table()
    
    thread1 = WorkerThread(db_operations)
    thread2 = WorkerThread(db_operations)
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()

    db_operations.close()

if __name__ == "__main__":
    main()