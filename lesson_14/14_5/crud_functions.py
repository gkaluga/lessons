import sqlite3


connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    );   
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    );
    ''')

    count = cursor.execute('SELECT COUNT(*) FROM Products').fetchone()[0]
    if count == 0:
        for i in range(1, 5):
            cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                           (f'Продукт {i}', f'Описание {i}', i * 100))
    connection.commit()

def get_all_products():
    return cursor.execute('SELECT * FROM Products').fetchall()

def get_product(id):
    return cursor.execute('SELECT * FROM Products WHERE id = ?',(id,)).fetchone()

def is_included(username):
    r = cursor.execute('SELECT COUNT(*) FROM Users WHERE username = ?', (username,)).fetchone()
    return r[0] > 0

def add_user(username, email, age):
    if is_included(username):
        return False
    else:
        cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                       (username, email, age, 1000))
        connection.commit()
        return True
