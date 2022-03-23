import datetime as dt
import pandas as pd
from typing import List, Tuple

class RawFreqDataCreator:

    def __init__(self, dbHost, dbUser, dbUserPass, dbName):
        self.dbHost = dbHost
        self.dbUser = dbUser
        self.dbUserPass = dbUserPass
        self.dbName = dbName

    def readRawFreqExcel(self, targetDate:dt.datetime):
        # read excel for target date and return dataframe
        print(f"read excel for {targetDate} and return dataframe")
        return pd.DataFrame()

    def convertExlToRecords(self, excelDf:pd.DataFrame)->List[Tuple]:
        # convert excel to list of tuple
        print(f"convert excel of to list of tuple")
        return [(), ()]

    def insertRecordToDB(self, freqRecords:List[Tuple])->bool:
        
        # push list of tuple of frequency record to database
        print(f"push list of tuple of frequency record of to database")
        return True 
    
    def createRawFrequency(self, targetDate:dt.datetime)->bool:
        freqDf =self.readRawFreqExcel(targetDate)
        freqRecord = self.convertExlToRecords(freqDf)
        isInsetionSuccess = self.insertRecordToDB(freqRecord)
        return isInsetionSuccess
        
