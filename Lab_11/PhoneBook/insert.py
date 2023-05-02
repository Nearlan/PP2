import psycopg2
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


def show():
    
    sql = f'''
    
   CREATE procedure delete(n VARCHAR(20), e VARCHAR(20))
    LANGUAGE plpgsql
AS
$$
BEGIN
    INSERT INTO phone (name, number)
    SELECT * FROM (SELECT n AS name, e AS number) AS temp
    WHERE NOT EXISTS (
    SELECT name FROM stats WHERE name = n
) LIMIT 1;
END;
$$;


    '''
    cursor.execute(sql)


show()