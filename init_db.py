import sqlite3

# connect or create the database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# create the post table
c.execute('''
    CREATE TABLE IF NOT EXISTS posts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL
)
''')


conn.commit()
conn.close()

print("Database iniatilized")