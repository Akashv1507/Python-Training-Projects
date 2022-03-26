import datetime as dt
from multiprocessing import connection
import pandas as pd
from typing import List, Tuple
import mysql.connector

class DerFreqDataCreator:

    def __init__(self, dbHost, dbUser, dbUserPass, dbName, excelFilePath):
        self.dbHost = dbHost
        self.dbUser = dbUser
        self.dbUserPass = dbUserPass
        self.dbName = dbName
        self.excelFilePath = excelFilePath

    def readRawFreqDb(self, targetDate:dt.datetime)->pd.DataFrame:
        
        startTime = targetDate.replace(hour=0, minute=0, second=0)
        endTime = startTime+ dt.timedelta(hours=23, minutes=59, seconds=59)
        startTimeStr = str(startTime)
        endTimeStr = str(endTime)
        try:
            conn = mysql.connector.connect(host =self.dbHost, user =self.dbUser, passwd =self.dbUserPass, database = self.dbName)
            # preparing a cursor object
            cursor = conn.cursor()
        except Exception as err:
            print(f"database connection/cursor unsuccessfull err thrown is {err}")
        
        else:
            #bind parameter
            fetchSql = "SELECT Time_STAMP, VALUE FROM Raw_Frequency WHERE TIME_STAMP Between %(start_Time)s and %(end_Time)s order by time_stamp"
            #fetch data directly to dataframe
            rawFreDf =pd.read_sql(fetchSql,params={'start_Time':startTimeStr,'end_Time':endTimeStr}, con= conn)
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        return rawFreDf

    def convertDfToDervideParams(self, rawFreqDf:pd.DataFrame, targetDate:dt.datetime)->List[Tuple]:
        # convert raw freq  to list of tuple of derived parameters of frequency
        
        maxFreq= rawFreqDf['VALUE'][0]
        minFreq= rawFreqDf['VALUE'][0]
        countLess = 0
        countGreat = 0
        sum = 0
        countRows = len(rawFreqDf)
        for ind in rawFreqDf.index:
            sum = sum + rawFreqDf['VALUE'][ind]
            if rawFreqDf['VALUE'][ind]>maxFreq:
                maxFreq= rawFreqDf['VALUE'][ind]
            if rawFreqDf['VALUE'][ind]<minFreq:
                minFreq= rawFreqDf['VALUE'][ind]
            if rawFreqDf['VALUE'][ind]>50.05:
                countGreat= countGreat+1
            if rawFreqDf['VALUE'][ind]<49.9:
                countLess= countLess+1

        avg = sum/countRows
        perLessBand = (countLess/countRows)*100
        perGreatBand = (countGreat/countRows)*100
        perBetweenBand = 100-(perLessBand+perGreatBand)
        perOutBand = perLessBand+perGreatBand
        hrsOutBand = (24*perOutBand)/100
        fdi = hrsOutBand/24

        derFreqParamTuple = (targetDate.date(), round(maxFreq,2), round(minFreq,2), round(avg,2), round(perLessBand,2), round(perBetweenBand,2), round(perGreatBand,2), round(perOutBand,2), round(hrsOutBand,2), round(fdi,2) )
        return derFreqParamTuple

    def insertRecordToDB(self, derFreqParamTuple:Tuple)->bool:
        
        # push list of tuple of frequency record to database
        isInsSuccess = True
        try:
            conn = mysql.connector.connect(host =self.dbHost, user =self.dbUser, passwd =self.dbUserPass, database = self.dbName)
            # preparing a cursor object
            cursor = conn.cursor()
        except Exception as err:
            print(f"database connection/cursor unsuccessfull err thrown is {err}")
            isInsSuccess= False
        else:
            # upsert ->update if present or insert if not.. deleting records based on unique column before insertion
            existingDerFreqRow = (derFreqParamTuple[0],)
            cursor.execute("delete from Derived_Frequency where datekey=%s", existingDerFreqRow)

            #bind parameter
            insertSql = "INSERT INTO Derived_Frequency (DATEKEY, MAXIMUM, MINIMUM, AVERAGE, LESS_THAN_BAND, BETWEEN_BAND, GREATER_THAN_BAND, OUT_OF_BAND, OUT_OF_BAND_INHRS, FDI) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            # to insert multiple record
            cursor.execute(insertSql, derFreqParamTuple)
            conn.commit()
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        return isInsSuccess 
    
    def createDerFrequency(self, targetDate:dt.datetime)->bool:

        derFreqDf =self.readRawFreqDb(targetDate)
        derFreqParamTuple =self.convertDfToDervideParams(derFreqDf, targetDate)
        isInsertionSuccess = self.insertRecordToDB(derFreqParamTuple)
        return isInsertionSuccess
        
