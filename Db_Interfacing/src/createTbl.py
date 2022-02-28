import mysql.connector

def createTbl(appConfig:dict):

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
        
        # creating table
        studentRecord = """CREATE TABLE STUDENT (
                        NAME  VARCHAR(20) NOT NULL,
                        BRANCH VARCHAR(50),
                        ROLL INT NOT NULL,
                        SECTION VARCHAR(5),
                        AGE INT
                        )"""
        
        # table created 
        cursor.execute(studentRecord)
        cursor.close()
        conn.close()
