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
    )    
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
