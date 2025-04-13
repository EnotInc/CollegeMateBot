import pandas as pd
import camelot

from .parser import get_link


def to_df(file):
    
    pdf = camelot.read_pdf(file)
    
    df = pdf[0].df
    df.columns = df.iloc[0]
    df = df.drop(0)
    df = df.reset_index(drop=True)

    return df


def get_all_schedules():
    course_0 = get_link(course=0, week=1)
    course_1 = get_link(course=1, week=1)
    course_2 = get_link(course=2, week=1)
    course_3 = get_link(course=3, week=1)
    
    course_0 = to_df(course_0)
    course_1 = to_df(course_1)
    course_2 = to_df(course_2)
    course_3 = to_df(course_3)

    course_0.to_csv('backend_logic/schedules/course_0.csv', sep=',', index=False)
    course_1.to_csv('backend_logic/schedules/course_1.csv', sep=',', index=False)
    course_2.to_csv('backend_logic/schedules/course_2.csv', sep=',', index=False)
    course_3.to_csv('backend_logic/schedules/course_3.csv', sep=',', index=False)


def get_schedule_as_df(course):
    df = pd.read_csv(f'backend_logic/schedules/course_{course}.csv')
    return df

def get_groups(course):
    df = pd.read_csv(f'backend_logic/schedules/course_{course}.csv')

    cdf = [col for col in df.columns if str(col).startswith("2")]

    return cdf