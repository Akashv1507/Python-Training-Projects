import datetime as dt
from typing import Dict
import datetime as dt
from src.derFreq.derFreqDataCreator import DerFreqDataCreator

def createDerFreq(startDate:dt.datetime, endDate:dt.datetime, appConfig:Dict)->bool:

    dbHost = appConfig["dbHost"]
    dbUser = appConfig["dbUser"]
    dbUserPass = appConfig["dbUserPass"]
    dbName = appConfig["dbName"]
    excelFilePath = appConfig["RawExcelPath"]

    obj_derFreqDataCreator = DerFreqDataCreator(dbHost, dbUser, dbUserPass, dbName, excelFilePath)

    currDate = startDate

    while currDate<=endDate:
        isInsertionSuccess =obj_derFreqDataCreator.createDerFrequency(currDate)
        currDate = currDate + dt.timedelta(days=1)

    return True
    