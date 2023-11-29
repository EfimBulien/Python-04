import sqlite3

connection = sqlite3.connect('library.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        login TEXT NOT NULL UNIQUE,
        name TEXT NOT NULL,
        password TEXT NOT NULL,
        address TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER NOT NULL,
        genre TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employee(
        id INTEGER PRIMARY KEY,
        login TEXT NOT NULL,
        name TEXT NOT NULL,
        password INTEGER NOT NULL,
        wage INTEGER NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS lendings(
        id INTEGER PRIMARY KEY,
        book_id INTEGER NOT NULL,
        users_id INTEGER NOT NULL,
        lend_date TEXT NOT NULL,
        return_date TEXT,
        FOREIGN KEY (book_id) REFERENCES books (id),
        FOREIGN KEY (users_id) REFERENCES users (id)
    )
''')

connection.commit()
connection.close()