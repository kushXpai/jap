import sqlite3
import threading

class DatabaseOperations:
    def __init__(self, db_name="test.db"):
        self.db_name = db_name

        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                         (id INTEGER PRIMARY KEY, 
                          name TEXT,
                          email TEXT,
                          age INTEGER)''')
        connection.commit()
        connection.close()

    def connect(self):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        return connection, cursor

    def create_user(self, name, email=None, age=None):
        """Create a new user with the given attributes"""
        connection, cursor = self.connect()
        try:
            cursor.execute('''INSERT INTO users (name, email, age) VALUES (?, ?, ?)''', 
                           (name, email, age))
            connection.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Error creating user: {e}")
            return None
        finally:
            connection.close()
    
    def insert_data(self, name):
        return self.create_user(name)

    def get_all_users(self):
        """Get all users from the database"""
        connection, cursor = self.connect()
        try:
            cursor.execute('''SELECT * FROM users''')
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error fetching users: {e}")
            return []
        finally:
            connection.close()
    
    def get_user_by_id(self, user_id):
        """Get a specific user by ID"""
        connection, cursor = self.connect()
        try:
            cursor.execute('''SELECT * FROM users WHERE id = ?''', (user_id,))
            result = cursor.fetchone()
            return result
        except Exception as e:
            print(f"Error fetching user by ID: {e}")
            return None
        finally:
            connection.close()
    
    def get_users_by_name(self, name):
        """Get users by name (can return multiple results)"""
        connection, cursor = self.connect()
        try:
            cursor.execute('''SELECT * FROM users WHERE name LIKE ?''', (f"%{name}%",))
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error fetching users by name: {e}")
            return []
        finally:
            connection.close()

    def fetch_data(self):
        return self.get_all_users()

    def update_user(self, user_id, name=None, email=None, age=None):
        """Update user information"""
        connection, cursor = self.connect()
        try:
            cursor.execute('''SELECT name, email, age FROM users WHERE id = ?''', (user_id,))
            current_data = cursor.fetchone()
            
            if not current_data:
                print(f"User with ID {user_id} not found")
                return False
                
            current_name, current_email, current_age = current_data
            new_name = name if name is not None else current_name
            new_email = email if email is not None else current_email
            new_age = age if age is not None else current_age
            
            cursor.execute('''UPDATE users SET name = ?, email = ?, age = ? WHERE id = ?''', 
                          (new_name, new_email, new_age, user_id))
            connection.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error updating user: {e}")
            return False
        finally:
            connection.close()

    def delete_user(self, user_id):
        """Delete a user by ID"""
        connection, cursor = self.connect()
        try:
            cursor.execute('''DELETE FROM users WHERE id = ?''', (user_id,))
            connection.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False
        finally:
            connection.close()
            
    def delete_all_users(self):
        """Delete all users (use with caution)"""
        connection, cursor = self.connect()
        try:
            cursor.execute('''DELETE FROM users''')
            connection.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"Error deleting all users: {e}")
            return 0
        finally:
            connection.close()

class WorkerThread(threading.Thread):
    def __init__(self, db_operations, thread_id):
        threading.Thread.__init__(self)
        self.db_operations = db_operations
        self.thread_id = thread_id
    
    def run(self):
        print(f"\n=== Thread {self.thread_id} starting CRUD operations ===")
        
        user1_id = self.db_operations.create_user(f"John Doe {self.thread_id}", 
                                                f"john{self.thread_id}@example.com", 
                                                30 + self.thread_id)
        user2_id = self.db_operations.create_user(f"Jane Smith {self.thread_id}", 
                                                f"jane{self.thread_id}@example.com", 
                                                25 + self.thread_id)
        
        print(f"Thread {self.thread_id} created users with IDs: {user1_id}, {user2_id}")
        
        print(f"Thread {self.thread_id} reading all users:")
        all_users = self.db_operations.get_all_users()
        for user in all_users:
            print(f"  {user}")
            
        user = self.db_operations.get_user_by_id(user1_id)
        print(f"Thread {self.thread_id} found user by ID {user1_id}: {user}")
        
        updated = self.db_operations.update_user(user1_id, 
                                              name=f"John Updated {self.thread_id}",
                                              age=35 + self.thread_id)
        
        print(f"Thread {self.thread_id} updated user {user1_id}: {updated}")
        
        updated_user = self.db_operations.get_user_by_id(user1_id)
        print(f"Thread {self.thread_id} verified update: {updated_user}")
        
        deleted = self.db_operations.delete_user(user2_id)
        print(f"Thread {self.thread_id} deleted user {user2_id}: {deleted}")
        
        final_users = self.db_operations.get_all_users()
        print(f"Thread {self.thread_id} final users list:")
        for user in final_users:
            print(f"  {user}")



print("Initializing database...")
db_operations = DatabaseOperations()
deleted_count = db_operations.delete_all_users()
print(f"Cleared {deleted_count} previous user records")

threads = []
for i in range(3):
    thread = WorkerThread(db_operations, i)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("\n=== Final database contents ===")
final_db = DatabaseOperations()
all_users = final_db.get_all_users()
for user in all_users:
    print(f"User ID: {user[0]}, Name: {user[1]}, Email: {user[2]}, Age: {user[3]}")

print(f"\nTotal users in database: {len(all_users)}")
