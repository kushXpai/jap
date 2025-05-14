import sqlite3
import threading

class DatabaseOperations:
    def __init__(self, db_name="test.db"):
        self.db_name = db_name

        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
        connection.commit()
        connection.close()
        
    def connect(self):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        return connection, cursor
        
    def insert_data(self, name, age):
        connection, cursor = self.connect()
        try:
            cursor.execute('''INSERT INTO users (name, age) VALUES (?, ?)''', (name, age))
            connection.commit()
        except Exception as e:
            print(f"Error inserting data: {e}")
        finally:
            connection.close()
            
    def fetch_data(self):
        connection, cursor = self.connect()
        try:
            cursor.execute('''SELECT * FROM users''')
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error fetching data: {e}")
            return []
        finally:
            connection.close()

class WorkerThread(threading.Thread):
    def __init__(self, db_operations, thread_id, data_to_insert):
        threading.Thread.__init__(self)
        self.db_operations = db_operations
        self.thread_id = thread_id
        self.data_to_insert = data_to_insert
        
    def run(self):
        for name, age in self.data_to_insert:
            self.db_operations.insert_data(name, age)
            print(f"Thread {self.thread_id} inserted: {name}, {age}")
        
        result = self.db_operations.fetch_data()
        print(f"Thread {self.thread_id} sees: {result}")

def main():
    db_operations = DatabaseOperations()

    print("Enter names and ages to insert into the database (type 'done' when finished):")
    user_input = []
    while True:
        name = input("Enter name: ")
        if name.lower() == 'done':
            break
        age = input(f"Enter age for {name}: ")
        try:
            age = int(age)
            user_input.append((name, age))
        except ValueError:
            print("Please enter a valid age.")
    
    if not user_input:
        print("No input provided, using default data.")
        user_input = [("John Doe", 30), ("Jane Smith", 25), ("Alice Johnson", 28), ("Bob Brown", 35)]

    num_threads = 2
    data_chunks = [[] for _ in range(num_threads)]
    
    for i, (name, age) in enumerate(user_input):
        chunk_index = i % num_threads
        data_chunks[chunk_index].append((name, age))
    
    threads = []
    for i in range(num_threads):
        thread = WorkerThread(db_operations, i, data_chunks[i])
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print("\nFinal database contents:")
    final_db = DatabaseOperations()
    print(final_db.fetch_data())

if __name__ == "__main__":
    main()