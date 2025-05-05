import requests
import os
import re

from datetime import date, datetime
from dotenv import load_dotenv


from backend_logic.ASCII_the_cat import cat

load_dotenv()


headers = {
        "Accept": os.getenv('ACCEPT'),
        "User-Agent": os.getenv('USER_AGENT')
}
url = os.getenv('URL')


def get_link(course=0, week=0):
    s = requests.Session()

    response = s.get(url=url)
    jres = response.json()
    s.close()

    try:
        for i in range(12):
            req = jres['data']['folders'][2]['files'][i]
            
            altName = req.get('altName')
            link = os.getenv('LINK')+req.get('src')
            
            first_date, last_date = parse_dates(req.get('title'))

            this_week = is_in_this_week(first_date=first_date, last_date=last_date)

            if altName[:10] == 'raspisanie' and int(altName[26]) == course+1 and this_week * (1-week):
                return link

    except Exception as ex:
        print(f'Error in parser:\n{ex}')
        return None


def parse_dates(text): 
    date_pattern = r'\d{2}\.\d{2}'
    dates = re.findall(date_pattern, text)
    
    this_yaer = date.today().year

    first_date = f'{dates[0]}.{this_yaer}'
    last_date = f'{dates[1]}.{this_yaer}'

    return first_date, last_date


def is_in_this_week(first_date, last_date):
    date_format = '%d.%m.%Y'

    first_date_format = datetime.strptime(first_date, date_format).date()
    last_date_format = datetime.strptime(last_date, date_format).date()

    today = date.today()
    in_this_week = first_date_format <= today <= last_date_format

    return in_this_week


def get_today_schedule(course, group):

    from backend_logic.schedule_constructor import get_schedule_as_df
    df = get_schedule_as_df(course=course)

    column_index = df.columns.get_loc(group)
    subjects_info = []
    day_of_week = date.today().weekday()

    lession_time = ['9:00 - 10:30', '10:50 - 11:35 & 11:55 - 12:40', '13:00 - 14:30', '14:50 - 16:20', '16:30 - 18:00']
    if day_of_week == 5 or day_of_week == 6:
        subjects_info.append('Сегодня выходной')
        return subjects_info
    
    try:
        for j in range(1, 6):
            i = j + 5*day_of_week
            main_string: str = df[df.columns[column_index]].iloc[i]
            
            general_info = main_string.split('\n')

            index = main_string.rfind('\n')
            subject = main_string[:index].replace('\n','')

            if(subject==''):
                continue

            if(subject=='ПРАКТИК'):
                subjects_info = []
                subjects_info.append('У вас практика, а это значит что расписание следует уточнить у преподавателя')
                break

            if('Разговоры' in subject):
                subject += 'важном"'
                subjects_info.append(f':books: Пара №{i} - {subject}\n\n:watch: Время пары: {lession_time[j-1]}')
            else:
                teacher = general_info[len(general_info)-1]
                classroom = df.iloc[:,column_index+1].tolist()[i]
                subjects_info.append(f':books: Пара №{j} - {subject}\
                    \n\n:teacher: Преподаватель: {teacher}\
                    \n\n:door: Аудитория: {classroom}\
                    \n\n:watch: Время пары: {lession_time[j-1]}')
    except Exception as ex:
        print('Error at scheduler contrtuc loop (for)')
        print(ex)

    return subjects_info
