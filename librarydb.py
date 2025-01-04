import psycopg2

def connect_to_postgres():
    """Connect to the default 'postgres' database."""
    return psycopg2.connect(
        host="localhost",
        user="postgres",
        password="Sps@2512",
        port=5432,
        database="postgres"  # Connect to the 'postgres' database
    )

def connect_to_library():
    """Connect to the 'library' database."""
    return psycopg2.connect(
        host="localhost",
        user="postgres",
        password="Sps@2512",
        port=5432,
        database="library"
    )

# Step 1: Connect to the default 'postgres' database
db1 = connect_to_postgres()

# Enable autocommit for non-transactional commands
db1.autocommit = True
c1 = db1.cursor()

# Drop the 'library' database if it exists
try:
    c1.execute("DROP DATABASE IF EXISTS library")
    print("Dropped 'library' database if it existed.")
except Exception as e:
    print("Error while dropping database:", e)

# Create the 'library' database
try:
    c1.execute("CREATE DATABASE library")
    print("Created 'library' database.")
except Exception as e:
    print("Error while creating database:", e)

# Close the connection to 'postgres'
c1.close()
db1.close()

# Step 2: Reconnect to the newly created 'library' database
db1 = connect_to_library()
c1 = db1.cursor()

# Step 3: Create tables and insert data
try:
    c1.execute("""
    CREATE TABLE users (
        username VARCHAR(30),
        passw VARCHAR(30)
    )
    """)
    c1.execute("INSERT INTO users (username, passw) VALUES ('Anjali', 'abc123')")
    c1.execute("INSERT INTO users (username, passw) VALUES ('Rahul', 'xyz123')")
    c1.execute("INSERT INTO users (username, passw) VALUES ('Aarav', 'pqr123')")

    c1.execute("""
    CREATE TABLE member (
        mid VARCHAR(20) PRIMARY KEY,
        name VARCHAR(50),
        email VARCHAR(50),
        phone VARCHAR(20)
    )
    """)
    c1.execute("""
    CREATE TABLE book (
        bookid VARCHAR(20) PRIMARY KEY,
        title VARCHAR(50),
        author VARCHAR(50),
        publisher VARCHAR(50),
        cost INTEGER
    )
    """)
    c1.execute("""
    CREATE TABLE issue (
        mid VARCHAR(20),
        bookid VARCHAR(20),
        dateofissue DATE
    )
    """)
    c1.execute("""
    CREATE TABLE issuelog (
        mid VARCHAR(20),
        bookid VARCHAR(20),
        dateofissue DATE,
        dateofreturn DATE
    )
    """)
    db1.commit()
    print("Database and tables created successfully.")
except Exception as e:
    print("Error while creating tables or inserting data:", e)

# Close the connection
c1.close()
db1.close()

