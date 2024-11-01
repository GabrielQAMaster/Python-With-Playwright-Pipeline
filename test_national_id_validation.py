import pyodbc
from playwright.sync_api import sync_playwright
import re

def query_national_id_with_letters():
    # Connection string for AdventureWorks2022 database
    connection_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"  # Update server name if necessary
        "DATABASE=AdventureWorks2022;"  # Ensure this matches your database
        "Trusted_Connection=yes;"
    )

    # Connect to the database
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()

        # Query to fetch NationalID data
        cursor.execute("SELECT NationalIDNumber FROM HumanResources.Employee")
        national_ids = cursor.fetchall()
        
        # Find any NationalID with letters using a regex pattern
        invalid_national_ids = [nid[0] for nid in national_ids if re.search(r'[A-Za-z]', nid[0])]
        
        return invalid_national_ids

def test_national_id_validation():
    # Run the query to find any invalid NationalID entries
    invalid_national_ids = query_national_id_with_letters()

    # Log the result to a txt file
    with open("national_id_validation_results.txt", "w") as file:
        if invalid_national_ids:
            file.write("National IDs with letters detected:\n")
            for nid in invalid_national_ids:
                file.write(f"{nid}\n")
        else:
            file.write("No National IDs with letters found. All entries are valid.\n")

    # Return the results for optional further use
    return invalid_national_ids

# Run the test function
if __name__ == "__main__":
    invalid_national_ids = test_national_id_validation()
    if invalid_national_ids:
        print("Some National ID entries contain letters. See national_id_validation_results.txt for details.")
    else:
        print("All National ID entries are valid. No letters found.")
