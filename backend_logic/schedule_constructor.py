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

    for i in range(4):
        course = get_link(course=i, week=1)
        course = to_df(course)
        course.to_csv(f'backend_logic/schedules/course_{i}.csv', sep=',', index=False)
    
def get_schedule_as_df(course):
    df = pd.read_csv(f'backend_logic/schedules/course_{course}.csv')
    return df


def get_groups(course):
    df = pd.read_csv(f'backend_logic/schedules/course_{course}.csv')

    cleared_df = [col for col in df.columns if str(col).startswith("2")]

    return cleared_df