import psycopg2

db1 = None

def connect():
    global db1
    db1 = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="root",
        port=5432
    )

connect()
c1 = db1.cursor()

# Drop database (if you have sufficient permissions, otherwise skip this step)
c1.execute("DROP DATABASE IF EXISTS library")

# Create database
c1.execute("CREATE DATABASE library")
db1.commit()

# Reconnect to the newly created database
db1.close()
db1 = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="root",
    port=5432,
    database="library"
)
c1 = db1.cursor()

# Create tables and insert data
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

# Close the connection
c1.close()
db1.close()
