import mysql.connector
from typing  import List, Tuple

def deleteMultipleUniqueRecord(appConfig:dict, listOfNames:List[Tuple]):
    
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
        delSql = " DELETE FROM STUDENT WHERE Name = %s and age =%s "
        cursor.executemany(delSql, listOfNames)
        conn.commit()

        if cursor:
            cursor.close()
        if conn:
            conn.close()