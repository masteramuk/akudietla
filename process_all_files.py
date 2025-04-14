import os
import pandas as pd
import sqlite3
from tabula import read_pdf

# Folder containing files
data_folder = '../sampledata/'

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