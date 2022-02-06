import requests
import datetime as dt

# stateId = 21
# districtId = 395

# two methods to pass parameters in api by using body of request , and second one bys using query parameters in url

def getSessionsInDistrict(distId, dateObj):
    # dateStr = dt.datetime.strftime(dateObj, "%d-%m-%Y")
    resp = requests.get(f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={distId}&date={dateObj}')
    if not resp.status_code == 200:
        print(resp.status_code)
        print("unable to get data from server")
        return []
    respJson = resp.json()
    sessions = respJson["sessions"]
    if len(sessions) == 0:
        return []
    return sessions