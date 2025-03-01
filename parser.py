import requests
import os

from datetime import date, datetime


headers = {
        "Accept": os.getenv('ACCEPT'),
        "User-Agent": os.getenv('USER_AGENT')
}

url = os.getenv('URL')


def get_link(course=0, week=0):
    s = requests.Session()

    response = s.get(url=url, headers=headers)
    jres = response.json()
    s.close()

    try:
        for i in range(12):
            req = jres['data']['folders'][2]['files'][i]
            
            altName = req.get('altName')
            link = os.getenv('LINK')+req.get('src')
            last_date = req.get('title')[-10:]

            if altName[:10] == 'raspisanie':
                if date_diff(last_date) < 5 and week == 0 and int(altName[26]) == course+1:
                    return link
                elif date_diff(last_date) >= 5 and week == 1 and int(altName[26]) == course+1:
                    return link
            else:
                return None 

    except Exception as ex:
        print(f'Error in parser:\n{ex}')
        return None


def date_diff(getted_date):
    date_format = '%d.%m.%Y'

    date1 = datetime.strptime(getted_date, date_format).date()
    today = date.today()

    delta = date1 - today 
    return delta.days
