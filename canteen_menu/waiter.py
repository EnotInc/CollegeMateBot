import enum
from datetime import date, datetime


class emotion(enum.Enum):
        default = 0
        bad = 1
        mid = 2
        good = 3
        best = 4

menu_chedule_emotions = {
        0 : emotion.mid.value,
        1 : emotion.default.value,
        2 : emotion.mid.value,
        3 : emotion.good.value,
        4 : emotion.bad.value,
        6 : emotion.good.value,
        7 : emotion.mid.value,
        8 : emotion.bad.value,
        9 : emotion.mid.value,
        10: emotion.best.value
}

ascii_cat = [

        '|\\_ _ _/|\
        \n| o w o|',

        '|\\_ _ _/|\
        \n|  x _ x |',

        '|\\_ _ _/|\
        \n| o = o |',

        '|\\_ _ _/|\
        \n| ^ W ^ |',

        '|\\_ _ _/|\
        \n| * w * |',
]

beginning_date = '04.03.2025'

def get_menu():
        date_format = '%d.%m.%Y'

        day_of_week = date.today().weekday()
        date1 = datetime.strptime(beginning_date, date_format).date()

        delta = date1 - date.today()

        weeks_past = delta.days//7
        day_of_menu = weeks_past%2 * 6 + day_of_week

        return day_of_menu

