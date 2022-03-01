import mysql.connector

def deleteRecord(appConfig:dict, name:str):
    
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
        delSql = " DELETE FROM STUDENT WHERE Name = %(bName)s "
        cursor.execute(delSql, {"bName": name})
        conn.commit()

        if cursor:
            cursor.close()
        if conn:
            conn.close()