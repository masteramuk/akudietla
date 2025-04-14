# Step 2: Building and Testing the Dietary Database

This document explains the process of creating an SQLite database, reading data from various file formats (CSV, Excel, PDF), uploading the data into the database, and verifying whether the data was successfully loaded. This step ensures that all datasets are centralized in a single database for use by the Malaysian Dietary Recommendation Application (`akudietla`).

---

## **2.1 Creating the SQLite Database**

### **Objective**
The goal is to create a centralized SQLite database (`dietary.db`) where all data from multiple files (CSV, Excel, PDF) will be stored in separate tables.

### **Dataset processing**
1. **Retrieve from online available sources for sample data**

## database nutrition
- https://www.fao.org/infoods/infoods/tables-and-databases/asia/en/

**to crawl**
- https://www.fao.org/4/X6878E/X6878E35.htm#grp1
- https://www.fao.org/4/X6878E/X6878E34.htm#secc
- https://www.fao.org/4/X6878E/X6878E33.htm#secb
- https://www.fao.org/4/X6878E/X6878E27.htm#seca
- https://www.fao.org/4/x5557e/x5557e04.htm#cereals
- https://www.fao.org/4/x5557e/x5557e0a.htm#meat%20and%20meat%20products
- https://www.fao.org/4/x5557e/x5557e08.htm#fresh%20vegetables
- https://www.fao.org/4/x5557e/x5557e0b.htm#eggs
- https://www.fao.org/4/x5557e/x5557e0c.htm#fish%20and%20shellfish
- https://www.fao.org/4/x5557e/x5557e0d.htm#milk%20and%20cheese
- https://www.fao.org/4/x5557e/x5557e0e.htm#oils%20and%20fats
- https://www.fao.org/4/x5557e/x5557e0f.htm#miscellaneous
- https://www.fao.org/4/x5557e/x5557e06.htm#sugars%20and%20syrups
- https://www.fao.org/4/x5557e/x5557e0g.htm#cereals
- https://www.fao.org/4/x5557e/x5557e0h.htm#starches%20and%20starchy%20roots
- https://www.fao.org/4/x5557e/x5557e0i.htm#sugars%20and%20syrups
- https://www.fao.org/4/x5557e/x5557e0j.htm#pulses,%20nuts,%20and%20seeds
- https://www.fao.org/4/x5557e/x5557e0k.htm#fresh%20vegetables
- https://www.fao.org/4/x5557e/x5557e0l.htm#fruits
- https://www.fao.org/4/x5557e/x5557e0m.htm#meat%20and%20meat%20products
- https://www.fao.org/4/x5557e/x5557e0n.htm#eggs
- https://www.fao.org/4/x5557e/x5557e0o.htm#fish%20and%20shellfish
- https://www.fao.org/4/x5557e/x5557e0p.htm#milk%20and%20cheese
- https://www.fao.org/4/x5557e/x5557e0q.htm#oils%20and%20fats
- https://www.fao.org/4/x5557e/x5557e0r.htm#miscellaneous
- https://www.fatsecret.com/calories-nutrition/generic/nasi-lemak
- https://www.snapcalorie.com/nutrition/roti_canai_nutrition.html

2. **Data cleansing and removing irrelevant dataset**

### **Database Creation and Data Upload**
1. **Connect to SQLite Database**:
   - Use Python's `sqlite3` library to create and connect to the SQLite database.
   - If the database file (`dietary.db`) does not exist, it will be automatically created.

```python
import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('dietary.db')
conn.close()

print("SQLite database 'dietary.db' has been created.")
```

---

## **2.2 Reading Files and Uploading Data into the Database**

### **Objective**
Process all files in the `data/` folder and its subfolders, dynamically generate field names, create tables for each file, and insert data into the corresponding tables.

### **File Types Supported**
- **CSV Files**: Processed using `pandas.read_csv()`.
- **Excel Files**: Processed using `pandas.read_excel()`.
- **PDF Files**: Tables extracted using `tabula-py`, and text extracted using `pdfplumber`.

### **Steps**
1. **Traverse the Folder Structure**:
   - Use `os.walk()` to recursively scan the `data/` folder and its subfolders for files.

2. **Process Each File**:
   - For each file, determine its type (CSV, Excel, PDF).
   - Read the file and extract data.
   - Dynamically generate field names if headers are missing.
   - Create a table for the file in the SQLite database.
   - Insert the data into the table.

3. **Handle Special Characters in Table Names**:
   - Escape table names with double quotes (`"`) to handle special characters or spaces.

Here’s the Python script used to process all files:

```python
import os
import pandas as pd
import sqlite3
from tabula import read_pdf

# Folder containing files
data_folder = 'data/'

# Function to generate unique field names
def generate_field_names(num_columns):
    return [f"field_{i+1}" for i in range(num_columns)]

# Function to process a single file
def process_file(file_path, table_name, conn):
    try:
        # Determine file type
        if file_path.endswith(('.csv', '.xls', '.xlsx')):
            print(f"Processing Excel/CSV file: {file_path}")

            # Read CSV or Excel file
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            else:
                df = pd.read_excel(file_path)

            # Check if the first row contains headers
            if df.columns.str.contains('^Unnamed').any():
                print("No headers found. Generating unique field names.")
                df.columns = generate_field_names(len(df.columns))
            else:
                print("Headers found. Using them as field names.")

            # Create table and insert data
            df.to_sql(table_name, conn, if_exists='replace', index=False)
            print(f"Successfully processed file: {file_path} -> Table: {table_name}")

        elif file_path.endswith('.pdf'):
            print(f"Processing PDF file: {file_path}")

            # Extract tables from PDF using tabula-py
            tables = read_pdf(file_path, pages='all', multiple_tables=True)

            if not tables:
                print(f"No tables found in PDF: {file_path}")
                return

            for i, table in enumerate(tables):
                # Generate a unique table name for each table in the PDF
                pdf_table_name = f"{table_name}_table_{i+1}"

                # Check if the first row contains headers
                if table.columns.str.contains('^Unnamed').any():
                    print(f"No headers found in PDF table {i+1}. Generating unique field names.")
                    table.columns = generate_field_names(len(table.columns))
                else:
                    print(f"Headers found in PDF table {i+1}. Using them as field names.")

                # Create table and insert data
                table.to_sql(pdf_table_name, conn, if_exists='replace', index=False)
                print(f"Successfully processed PDF table: {pdf_table_name}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Main function to process all files
def main():
    # Connect to SQLite database
    conn = sqlite3.connect('dietary.db')

    # Walk through the folder and subfolders
    for root, dirs, files in os.walk(data_folder):
        print(f"Scanning folder: {root}")
        for filename in files:
            file_path = os.path.join(root, filename)
            table_name = filename.split('.')[0].replace(' ', '_')  # Use filename as table name

            print(f"Found file: {file_path}")
            process_file(file_path, table_name, conn)

    # Close the connection
    conn.close()
    print("All files have been processed and stored in the SQLite database.")

if __name__ == "__main__":
    main()
```

---

## **2.3 Testing the Database Upload**

### **Objective**
Verify that all tables and data have been successfully uploaded into the SQLite database.

### **Steps**
1. **List All Tables**:
   - Query the SQLite database to list all tables.

2. **Check Table Sizes**:
   - Count the number of rows in each table to confirm data insertion.

3. **Preview Table Contents**:
   - Display the first row of each table to verify the structure and content.

4. **Handle Errors Gracefully**:
   - Use error handling to debug problematic tables (e.g., tables with special characters or invalid schemas).

**Here’s the Python script used to test the database:**

```python
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
```

---

## **Key Notes**
1. **Dynamic Field Names**:
   - If headers are missing, unique field names like `field_1`, `field_2`, etc., are generated.

2. **Separate Tables for Each File**:
   - Each file (or table in a PDF) is stored as a separate table in the SQLite database.

3. **Error Handling**:
   - Problematic tables are identified using error messages and debugging tools like `PRAGMA table_info`.

4. **Centralized Database**:
   - The SQLite database (`dietary.db`) serves as the central repository for all datasets.

---

## **Next Steps**
Once the database is verified, we can proceed to:
1. **Develop the Recommendation Engine**: Use Hugging Face Transformers to generate personalized dietary advice based on the data in the SQLite database.
2. **Create the User Interface**: Build a CLI interface to collect user input and display recommendations.
