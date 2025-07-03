import sqlite3

print("a")
print(sqlite3.sqlite_version)

with sqlite3.connect("database.db") as conn:
    cursor = conn.cursor()

    
    cursor.execute('''DROP TABLE IF EXISTS book''')
    cursor.execute('''
        CREATE TABLE book(
            title TEXT,
            author TEXT,
            year INTEGER
        )
    ''')

    
    cursor.executemany("INSERT INTO book (title, author, year) VALUES (?, ?, ?)", [("Harry Potter", "JK Rowling", 2025), ("Hunger Games", "Suzanne Collins", 1900), ("Glass Castle", "Jeannette Walls", 1980)])

   
    conn.commit()

    print("\nBooks ordered by year:")
    for i in cursor.execute("SELECT * FROM book ORDER BY year"):
        print(i)

    print("\nAll books:")
    cursor.execute("SELECT * FROM book")
    res = cursor.fetchall()
    print(res)