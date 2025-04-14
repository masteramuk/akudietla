import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('dietary.db')
cursor = conn.cursor()

# List all tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Print the list of tables and their sizes
print("List of tables with sizes:")
for table in tables:
    table_name = table[0]
    
    # Escape table name using double quotes to handle special characters
    escaped_table_name = f'"{table_name}"'
    
    try:
        # Print the table name and size of it
        cursor.execute(f"SELECT COUNT(*) FROM {escaped_table_name};")
        row_count = cursor.fetchone()[0]
        print(f"Table: {table_name}, Rows: {row_count}")
        
        # Print the contents of each table
        print(f"\nContents of table '{table_name}':")
        cursor.execute(f"SELECT * FROM {escaped_table_name} LIMIT 1;")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        # Debugging table schema
        cursor.execute(f"PRAGMA table_info(\"{table_name}\");")
        schema = cursor.fetchall()
        print(f"Schema for table '{table_name}':")
        for column in schema:
            print(column)
    
        print(f"Error processing table '{table_name}': {e}")

# Print the total number of tables
total_tables = len(tables)
print(f"Total number of tables: {total_tables}")

# Close the connection
conn.close()