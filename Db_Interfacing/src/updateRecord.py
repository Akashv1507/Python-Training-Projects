import mysql.connector

def updateRecord(appConfig:dict, name:str, branch:str):
    
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
        updateSql = " UPDATE STUDENT SET branch =%(bBranch)s  WHERE Name = %(bName)s "
        cursor.execute(updateSql, {"bBranch":branch, "bName": name})
        conn.commit()

        if cursor:
            cursor.close()
        if conn:
            conn.close()