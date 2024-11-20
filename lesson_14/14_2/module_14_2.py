import sqlite3


connection = sqlite3.Connection('not_telegram.db')
cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS Users')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

for i in range(1, 11):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (f'User{i}', f'example{i}@gmail.com', i * 10, 1000))

for i in range(1, 11, 2):
    cursor.execute('UPDATE Users SET balance = ? WHERE username = ?',(500, f'User{i}'))

ids = cursor.execute('SELECT id FROM Users').fetchall()
for i in [x[0] for x in ids[::3]]:
    cursor.execute('DELETE FROM Users WHERE id = ?',(i,))

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?',(60,))
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} |  Возраст: {user[2]} | Баланс: {user[3]}')

cursor.execute('DELETE FROM Users WHERE id = ?',(6,))
connection.commit()

cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

cursor.execute('SELECT SUM(balance) FROM Users')
all_balances  = cursor.fetchone()[0]
print(all_balances / total_users)

connection.close()
