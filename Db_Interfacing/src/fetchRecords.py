import mysql.connector

def fetchRecords(appConfig:dict, age:int, branch:str ):
    
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
        fetchAllSql = "select * from student;"
        cursor.execute(fetchAllSql)
        allResult = cursor.fetchall()
        print(allResult)
        
        # prone to sql injection attack
        # fetchSql = f"select * from student where age < {age}"

        #bind parameter
        fetchSql = 'select * from student where age < %(bAge)s and branch = %(bBranch)s'
        cursor.execute(fetchSql, {"bBranch":branch, "bAge": age})
        myresult = cursor.fetchall()
        print(myresult)

        if cursor:
            cursor.close()
        if conn:
            conn.close()