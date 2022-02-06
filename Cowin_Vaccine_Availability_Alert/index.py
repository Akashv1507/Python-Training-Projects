from src.appConfig import getAppConfigDict
from src.seesionsDataFetcher import fetchSessionsByDistId
import datetime as dt
import argparse


# get apllication configuration dictionary
appConfig = getAppConfigDict()

noOfDays = appConfig['noOfDays']

# by default
startDate = dt.datetime.now()
endDate = startDate + dt.timedelta(days=noOfDays)

# get start and end dates from command line
parser = argparse.ArgumentParser()
parser.add_argument('--start_date', help="Enter start date in yyyy-mm-dd format",
                    default=dt.datetime.strftime(startDate, '%Y-%m-%d'))
parser.add_argument('--end_date', help="Enter end date in yyyy-mm-dd format",
                    default=dt.datetime.strftime(endDate, '%Y-%m-%d'))

args = parser.parse_args()
startDate = dt.datetime.strptime(args.start_date, '%Y-%m-%d')
endDate = dt.datetime.strptime(args.end_date, '%Y-%m-%d')

startDate = startDate.replace(
    hour=0, minute=0, second=0, microsecond=0)
endDate = endDate.replace(
    hour=0, minute=0, second=0, microsecond=0)

currDate= startDate

distIdsList = appConfig['districtIds']

for distId in distIdsList:
    while currDate<=endDate:
        sessions =fetchSessionsByDistId(distId, currDate )
        print(sessions[0]['district_name'], currDate)
        currDate = currDate + dt.timedelta(days=1)
    currDate= startDate

