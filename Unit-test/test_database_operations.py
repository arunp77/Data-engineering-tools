import unittest
import sqlite3

# Global variable to hold the database connection
db_connection = None

def setUpModule():
    """Set up a database connection before any tests in the module run."""
    global db_connection
    print("Setting up the database connection for the module...")
    db_connection = sqlite3.connect(":memory:")  # Use an in-memory database for testing

def tearDownModule():
    """Close the database connection after all tests in the module have run."""
    global db_connection
    print("Tearing down the database connection for the module...")
    db_connection.close()

class TestDatabase(unittest.TestCase):
    def setUp(self):
        """Create the table and populate it before each test."""
        cursor = db_connection.cursor()
        cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)''')
        cursor.executemany('INSERT INTO users (name) VALUES (?)', [('Alice',), ('Bob',)])
        db_connection.commit()

    def tearDown(self):
        """Drop the table after each test."""
        cursor = db_connection.cursor()
        cursor.execute('DROP TABLE users')
        db_connection.commit()

class TestUserOperations(TestDatabase):
    def test_user_count(self):
        """Test the number of users in the database."""
        cursor = db_connection.cursor()
        cursor.execute('SELECT COUNT(*) FROM users')
        count = cursor.fetchone()[0]
        self.assertEqual(count, 2)

    def test_user_names(self):
        """Test the names of the users in the database."""
        cursor = db_connection.cursor()
        cursor.execute('SELECT name FROM users')
        users = cursor.fetchall()
        self.assertEqual(users, [('Alice',), ('Bob',)])

class TestAdditionalUserOperations(TestDatabase):
    def test_add_user(self):
        """Test adding a new user to the database."""
        cursor = db_connection.cursor()
        cursor.execute('INSERT INTO users (name) VALUES (?)', ('Charlie',))
        db_connection.commit()
        
        cursor.execute('SELECT COUNT(*) FROM users')
        count = cursor.fetchone()[0]
        self.assertEqual(count, 3)

    def test_remove_user(self):
        """Test removing a user from the database."""
        cursor = db_connection.cursor()
        cursor.execute('DELETE FROM users WHERE name = ?', ('Alice',))
        db_connection.commit()

        cursor.execute('SELECT COUNT(*) FROM users')
        count = cursor.fetchone()[0]
        self.assertEqual(count, 1)

if __name__ == "__main__":
    unittest.main(verbosity=2)
