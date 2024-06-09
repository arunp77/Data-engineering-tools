import psycopg2

conn = psycopg2.connect( 
    database = "postgresql",
    user = "docker",
    password = "docker",
    host = "localhost"
)

# Open cursor to perform database operations
cur = conn.cursor()

# Query the database
cur.execute("""SELECT * FROM Student""")

rows = cur.fetchall()

if not len(rows):
    print("Empty")
else:      
    for row in rows:
        print(row)

# Close the communication with database: it makes sure that everything is closed when we are done using it.
cur.close()
conn.close()
