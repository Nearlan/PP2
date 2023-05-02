import psycopg2
from config import host, user, password, db_name


conn = psycopg2.connect(
    host = host,
    user = user,
    password = password,
    database = db_name
    )
conn.autocommit = True

cursor = conn.cursor()


f = open('demofile3.txt', 'r')
stats = f.read().split(sep = ',')
f.close()

def createtable():
    sql = '''
        CREATE TABLE Stats(
        name VARCHAR(5),
        score VARCHAR(20),
        level VARCHAR(2)
    )
    '''
    cursor.execute(sql)
    
def insertdata():
    
    sql = f'''
   INSERT INTO stats (name,score,level)
    SELECT * FROM (SELECT '{stats[0]}' AS name, '{stats[1]}' AS score, '{stats[2]}' AS lvl) AS temp
    WHERE NOT EXISTS (
    SELECT name FROM stats WHERE name = '{stats[0]}'
) LIMIT 1;
'''
    cursor.execute(sql)
    
    
    
def deletedatabyname():
    sql = f'''
    DELETE FROM stats WHERE name = '{stats[0]}';
    '''
    cursor.execute(sql)    
    
def updatedatabyname():

    sql = f''';
    UPDATE stats SET score = '{stats[1]}' WHERE name = '{stats[0]}';
    UPDATE stats SET level = '{stats[2]}' WHERE name = '{stats[0]}'
    '''
    cursor.execute(sql)    
    
#createtable()
insertdata()
updatedatabyname()
#deletedatabyname()