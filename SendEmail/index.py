# from src.emailSender import *
# from src.emailSenderImportEx import sendEmail, getData, dummyVar
from src.databaseConn import getDbConn
from src.appConfig import getAppConfigDict
from src.emailSender import sendEmail
import argparse

appConfigDict =getAppConfigDict()

fileName = 'file1.xlsx'

# get start and end dates from command line
parser = argparse.ArgumentParser()
parser.add_argument('--file_name', help="enter file name in xlsx",
                    default= fileName)

args = parser.parse_args()
argFileName = args.file_name


# making list of attachement file path
attachementList = []

# hardcoded , notused in real time scenerio
# file1= appConfigDict['filesPath']+'DeptWise-DSCs details.xlsx'
# file2 = appConfigDict['filesPath']+ 'Digital Signatures Details.xlsx'
# attachementList.append(file1)
# attachementList.append(file2)

fullFilePath = appConfigDict['filesPath']+ argFileName

attachementList.append(fullFilePath)

isMailSent = sendEmail(appConfigDict,'This is a test Mail', 'Hello!! this is as test mail body', attachementList)


if isMailSent:
    print('Mail sent successfully')
else:
    print('Mail sent unsuccessfully')


# print(appConfigDict)

# sendEmail()
# getData()
# getDbConn()



