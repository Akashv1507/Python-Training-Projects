import requests
import datetime as dt

# stateId = 21
# districtId = 395

# two methods to pass parameters in api by using body of request , and second one bys using query parameters in url

def getSessionsInDistrict(distId, dateObj):
    # dateStr = dt.datetime.strftime(dateObj, "%d-%m-%Y")
    resp = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict/',
                        params={"district_id": distId, "date": dateObj}, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
    
    if not resp.status_code == 200:
        print(resp.status_code)
        print("unable to get data from server")
        return []
    respJson = resp.json()
    sessions = respJson["sessions"]
    if len(sessions) == 0:
        return []
    return sessions