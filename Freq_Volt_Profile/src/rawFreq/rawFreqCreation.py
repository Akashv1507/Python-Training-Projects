import datetime as dt
from typing import Dict
from src.rawFreq.rawFreqDataCreator import RawFreqDataCreator
import datetime as dt

def createRawFreq(startDate:dt.datetime, endDate:dt.datetime, appConfig:Dict)->bool:

    dbHost = appConfig["dbHost"]
    dbUser = appConfig["dbUser"]
    dbUserPass = appConfig["dbUserPass"]
    dbName = appConfig["dbName"]
    excelFilePath = appConfig["RawExcelPath"]

    obj_rawFreqDataCreator = RawFreqDataCreator(dbHost, dbUser, dbUserPass, dbName, excelFilePath)

    currDate = startDate

    while currDate<=endDate:
        isInertionSuccess =obj_rawFreqDataCreator.createRawFrequency(currDate)
        currDate = currDate + dt.timedelta(days=1)

    return True
    



       
