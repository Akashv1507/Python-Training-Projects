import datetime as dt
import pandas as pd
from typing import List, Tuple
import mysql.connector

class RawFreqDataCreator:

    def __init__(self, dbHost, dbUser, dbUserPass, dbName, excelFilePath):
        self.dbHost = dbHost
        self.dbUser = dbUser
        self.dbUserPass = dbUserPass
        self.dbName = dbName
        self.excelFilePath = excelFilePath

    def readRawFreqExcel(self, targetDate:dt.datetime)->pd.DataFrame:
        # read excel for target date and return dataframe
        targetDateStr = dt.datetime.strftime(targetDate, '%d_%m_%Y')
        excelFileName = self.excelFilePath+ f'/Frequency_{targetDateStr}.xlsx'
        freqDf = pd.read_excel(excelFileName)
        return freqDf

    def convertExlToRecords(self, excelDf:pd.DataFrame)->List[Tuple]:
        # convert excel to list of tuple
        freqRecords = []
        for ind in excelDf.index:
            freqRecords.append((excelDf['timestamp'][ind], excelDf['frequency'][ind]))
        return freqRecords

    def insertRecordToDB(self, freqRecords:List[Tuple])->bool:
        
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
            existingFreqRows = [(x[0],) for x in freqRecords]
            cursor.executemany("delete from Raw_Frequency where TIME_STAMP=%s", existingFreqRows)

            #bind parameter
            insertSql = "INSERT INTO Raw_Frequency (TIME_STAMP, VALUE) VALUES (%s, %s)"
            # to insert multiple record
            cursor.executemany(insertSql, freqRecords)
            conn.commit()
            if cursor:
                cursor.close()
            if conn:
                conn.close()
        return isInsSuccess 
    
    def createRawFrequency(self, targetDate:dt.datetime)->bool:
        freqDf =self.readRawFreqExcel(targetDate)
        freqRecord = self.convertExlToRecords(freqDf)
        isInsetionSuccess = self.insertRecordToDB(freqRecord)
        return isInsetionSuccess
        
