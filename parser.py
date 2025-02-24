import requests
import os

from dotenv import load_dotenv


load_dotenv()

headers = {
        "Accept": os.getenv('ACCEPT'),
        "User-Agent": os.getenv('USER_AGENT')
}

url = os.getenv('URL')

def get_link(course=0, week=0):
    s = requests.Session()

    response = s.get(url=url, headers=headers)
    jres = response.json()

    try:
        req = jres['data']['folders'][2]['files'][course + 4*week]

        altName = req.get('altName')
        link = os.getenv('LINK')+req.get('src')

        if altName[:10] == 'raspisanie':
            return link
        else:
            return None

    except Exception as ex:
        print(ex)
        return None


def get_schedule_pdf(course=0, week=0):
    url = get_link(course=course, week=week)
    res = requests.get(url)

    with open('file.pdf', '+wb') as f:
        f.write(res.content)
   