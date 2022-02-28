from re import I
from src.appConfig import getAppConfigDict
from src.createTbl import createTbl
from src.insertOneRecord import insertOneRecord
import argparse


# doing CRUD operation , C=create, R= read, U=update, D= delete
appConfigDict =getAppConfigDict()

# createTbl(appConfigDict)

val = [("Ekta2", "CE", "03", "C", "22"),("Ekta3", "CE", "03", "C", "22"),("Ekta4", "CE", "03", "C", "22")]
insertOneRecord(appConfigDict, val)





