import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

cursor = conn.cursor()

# SQL query to create table
create_table_query = """
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    salary DECIMAL(10,2),
    hire_date DATE
)
"""

# Execute the query
cursor.execute(create_table_query)

print("Table created successfully!")

# Clean up
cursor.close()
conn.close()
