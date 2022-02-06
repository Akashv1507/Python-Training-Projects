import requests
import datetime as dt


def fetchSessionsByDistId(distId:str, dateObj:dt.datetime):

    # converting datetime to string
    dateStr = dt.datetime.strftime(dateObj, "%d-%m-%Y")
    
    sessions = []
    try:
        # making api call with request using distId and datestr as query parameter
        resp = requests.get('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict',
                            params={"district_id": distId, "date": dateStr}, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
        if resp.status_code==200:
            respObj = resp.json()
        else:
            respObj ={ 'session': []}
    except Exception as err:
        print(f"Api call unsuccessfull err thrown is {err}")
    else:
        sessions = respObj['sessions']
    finally:
        return sessions