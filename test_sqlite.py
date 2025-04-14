import sqlite3

# Test SQLite3 connection
try:
    conn = sqlite3.connect(':memory:')  # Creates an in-memory database for testing
    print("SQLite3 is working!")
    conn.close()
except Exception as e:
    print(f"Error: {e}")