import sqlite3
import hashlib
import os

#function to create  connection to sqlite3

def create_connection(db_file):
    conn=None
    try:
        conn=sqlite3.connect(db_file)
        print(f'Successfully connected to {db_file}')
        return conn
    except sqlite3.Error as e:
        print(e)
    
    return conn



#create a user table 

def create_user_table(conn):
    sql_statement='''CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name VARCHAR(20) NOT NULL UNIQUE,
        password VARCHAR(40) NOT NULL
        );    
    '''
    try:
        c=conn.cursor()
        c.execute(sql_statement)
        print('User table created successfully')
    except sqlite3.Error as e:
        print(e)

#create a expense table
        
def create_expense_table(conn):
    sql_statement='''CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER ,
    date DATETIME,
    amount DECIMAL,
    category TEXT,
    description TEXT,
    FOREIGN KEY (user_id) REFERENCES users (id)
    );
    '''
    try:
        c=conn.cursor()
        c.execute(sql_statement)
        print('Created expense table successfully')
    except sqlite3.Error as e:
        print(e)

#helper functions 
        
def hash_the_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

#register a user / sign up a user 

def register_user(username,password,conn):
    hashed_password=hash_the_password(password)
    sql_statement='''
        INSERT INTO users (user_name,password) VALUES(?,?)
        '''
    try:
        c=conn.cursor()
        c.execute(sql_statement,(username,hashed_password))
        conn.commit()
        print('User registerd successfully')
    except sqlite3.Error as e:
        print(e)

#authenticate the user 
        
def authenticate_user(username,password,conn):
    hashed_password=hash_the_password(password)
    sql_statement='''SELECT * FROM users WHERE user_name = ? AND password = ?'''
    try:
        c = conn.cursor()
        c.execute(sql_statement, (username, hashed_password))
        user = c.fetchone()
        if user:
            return user[0]  # Return user ID
        else:
            print("User not found , authentication failed")
            return None
    except sqlite3.Error as e:
        print(e)
    
# Function to log an expense
def log_expense(conn, user_id, date, amount, category, description):
    sql = '''INSERT INTO expenses (user_id, date, amount, category, description)
             VALUES (?, ?, ?, ?, ?)'''
    try:
        c = conn.cursor()
        c.execute(sql, (user_id, date, amount, category, description))
        conn.commit()
        print('Expense logged successfully')
    except sqlite3.Error as e:
        print(e)

def view_user_expenses(conn,user_id):
    sql='''SELECT * FROM expenses WHERE user_id= ?; '''
    try:
        c=conn.cursor()
        c.execute(sql,(user_id,))
        row = c.fetchone()
        print(row)
    except sqlite3.Error as e:
        print(e)
#main function 

def main():
    database = "expense_tracker.db"

    # Create a database connection
    conn = create_connection(database)

    if conn is not None:
        print("Connection to sqlite3 succesfull")
        create_user_table(conn)
        create_expense_table(conn)
    else:
        print("Error! Cannot create the database connection.")
        return
    print("Welcome to expense tracker \n below are the options and functionality\n 1.Register a user\n 2.Login for user\n")
    option_value=int(input("Enter the option\t"))
    if option_value==1:
            username=input("Enter username\t")
            password=input("Enter password\t")
            register_user(username,password,conn)
    elif option_value==2:
            username=input("Enter username\t")
            password=input("Enter password\t")
            res=authenticate_user(username,password,conn)
            if res is not None:
                print("Authentication successful. User ID:", res)
                # Now the user can log expenses
                print("1.Enter to log expense\n2.To view your expense records")
                log_or_view_expense=int(input("Enter the option to either log or view the expense\t"))
                match log_or_view_expense:
                    case 1:
                         date = input("Enter expense date (YYYY-MM-DD): \t")
                         amount = float(input("Enter expense amount:\t "))
                         category = input("Enter expense category:\t ")
                         description = input("Enter expense description:\t ")
                         log_expense(conn, res, date, amount, category, description)
                    case 2:
                         view_user_expenses(conn,res)

               
    else:
        print("invalid option")
    conn.close()


if __name__ == '__main__':
    main()

