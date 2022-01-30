# from src.emailSender import *
from src.emailSenderImportEx import sendEmail, getData, dummyVar
from src.databaseConn import getDbConn
from src.appConfig import getAppConfigDict
from src.emailSender import sendEmail


appConfigDict =getAppConfigDict()

isMailSent = sendEmail(appConfigDict,'This is a test Mail', 'Hello!! this is as test mail body')
if isMailSent:
    print('Mail sent successfully')
else:
    print('Mail sent unsuccessfully')


print(appConfigDict)

# sendEmail()
# getData()
# getDbConn()



