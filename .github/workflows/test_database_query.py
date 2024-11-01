import pyodbc
from playwright.sync_api import sync_playwright

def query_database():
    # Database connection details
    connection_string = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"  # Adjust server name if necessary
        "DATABASE=AdventureWorks2022;"  # Updated database name
        "Trusted_Connection=yes;"
    )

    # Connect to the database
    with pyodbc.connect(connection_string) as conn:
        cursor = conn.cursor()

        # Example query: Fetch top 10 products from the Product table
        cursor.execute("SELECT TOP 10 Name FROM Production.Product")
        products = cursor.fetchall()
        
        # Process the query results
        product_names = [row[0] for row in products]  # Extract product names from results
        return product_names

def test_database_query():
    # Run database query and get results
    product_names = query_database()

    # Log the result in a txt file
    with open("database_query_results.txt", "w") as file:
        file.write("Product Names from AdventureWorks2022:\n")
        for name in product_names:
            file.write(f"{name}\n")

    # Return the list for optional further processing
    return product_names

# Run the test function
if __name__ == "__main__":
    product_names = test_database_query()
    print("Query results saved in database_query_results.txt")
