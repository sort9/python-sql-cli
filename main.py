import mysql.connector
import getpass

# Collect Input
db_connection_string = input("Enter your connection string: ")
db_username = input("Enter your database username: ")
db_password = getpass.getpass("Enter your password: ") # Temp way to securely input password
selected_database = input("Enter your database name: ")

# Connection to SQL Server
try:
    mydb = mysql.connector.connect(
        host=db_connection_string,  # Localhost or IP Address of server
        user=db_username, # DB Username
        password=db_password, # DB Password associated with aforementioned username
        database=selected_database # DB to query
    )
    print("Connected to MySQL database!")

# Exception handling
except mysql.connector.Error as err:
    print(f"Error: {err}")

# Create a cursor object to execute a query on the database
cur = mydb.cursor()

# Use the cursor object to query the database
query = input("Enter your query: ")
cur.execute(query)

# Fetch all the results from the query and print them
query_results = cur.fetchall()
print(query_results)

# Close the connection
mydb.close()