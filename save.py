import sqlite3
running = True
with sqlite3.connect("names.db") as conn:
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS names(
            name TEXT,
            age INTEGER
        )
    ''')
    while running:
        close = input("Would you like to close the program?: ")
        if close == 'yes':
            running = False
        elif close == 'no':
            enter_name = input("Please Enter Your Name: ")
            enter_age = int(input("Enter age: "))
            cursor.execute("INSERT INTO names (name, age) VALUES (?, ?)", (enter_name, enter_age))
            for i in cursor.execute("SELECT * FROM names"):
                print(i[0], i[1])
            remove_name_option = input("Would you like to remove a name?: ")
            if remove_name_option == 'yes':
                remove_name = input("What name would you like to remove?: ")
                #cursor.execute("DELETE FROM names WHERE name = ?", (remove_name, enter_age))
                cursor.execute(DELETE FROM TABLE)
                conn.commit
                for i in cursor.execute("SELECT * FROM names"):
                    print(i[0], i[1])
        else:
            print('Invalid Input')
    
