from sqlite3 import connect

con = connect('data.db')

con.execute("""
    CREATE TABLE IF NOT EXISTS users(
        username TEXT PRIMARY KEY, password TEXT NOT NULL, auth BOOLEAN NOT NULL DEFAULT FALSE
    )
""")