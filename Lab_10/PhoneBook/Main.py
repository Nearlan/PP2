import psycopg2
import csv
from config import host, user, password, db_name

# Connect to database
conn = psycopg2.connect(
    host = host,
    user = user,
    password = password,
    database = db_name
    )
conn.autocommit = True

# Cursor
cursor = conn.cursor()


# Funcs
def createtable():
    sql = '''
        CREATE TABLE phone(
        name CHAR(20),
        number CHAR(12)
    )
    '''
    cursor.execute(sql)


def insertdata():
    name = input("Name to insert ")
    number = input("Number to insert ")
    sql = f'''
   INSERT INTO phone(name, number) VALUES
   ('{name}', '{number}')
'''
    cursor.execute(sql)

def insertfromcsv():
    with open("some.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            sql = f'''
                INSERT INTO phone(name, number) VALUES
                ('{row[0]}', '{row[1]}')
                '''
            cursor.execute(sql)


def updatedatabyname():
    find = input("Enter a name to find ")
    update = input("Enter a new number ")
    sql = f'''
    UPDATE phone SET number = '{update}' WHERE name = '{find}'
    '''
    cursor.execute(sql)
    
def updatedatabynumber():
    find = input("Enter a number to find ")
    update = input("Enter a new name ")
    sql = f'''
    UPDATE phone SET name = '{update}' WHERE number = '{find}'
    '''
    cursor.execute(sql)    
    
def deletedatabyname():
    find = input("Enter a name to delete ")
    sql = f'''
    DELETE FROM phone WHERE name = '{find}';
    '''
    cursor.execute(sql)
    
def show():
    filter = input("What you need to find ")
    sql = f'''
    SELECT * FROM phone WHERE name LIKE  '%{filter}%'
    '''
    cursor.execute(sql)
    result = cursor.fetchall()
    if result:
        print(result)
    else:
        sql = f'''
    SELECT * FROM phone WHERE number LIKE '%{filter}%'
    '''
        cursor.execute(sql)
        result = cursor.fetchall()
        if result:
            print(result)
        else:
            print('There are none')


#createtable()
#insertdata()
#deletedatabyname()
#updatedatabyname()
#updatedatabynumber()
#show()
#insertfromcsv()

# Closing connection 
conn.close()

