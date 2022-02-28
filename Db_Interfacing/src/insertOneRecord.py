import mysql.connector

def insertOneRecord(appConfig:dict, values):
    
    dbHost = appConfig["dbHost"]
    dbUser = appConfig["dbUser"]
    dbUserPass = appConfig["dbUserPass"]
    dbName = appConfig["dbName"]

    try:
        conn = mysql.connector.connect(host =dbHost, user =dbUser, passwd =dbUserPass, database = dbName)
    except Exception as err:
        print(f"database connection unsuccessfull err thrown is {err}")
    else:
        # preparing a cursor object
        cursor = conn.cursor()
        
        #bind parameter
        insertSql = "INSERT INTO STUDENT (NAME, BRANCH, ROLL, SECTION, AGE) VALUES (%s, %s, %s, %s, %s)"
        
        # to insert single record
        # cursor.execute(insertSql, values)
        # to insert multiple record
        cursor.executemany(insertSql, values)
        conn.commit()
        cursor.close()
        conn.close()