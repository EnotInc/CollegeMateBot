import camelot

from parser import get_link

def get_today_schedule(group):
    link = get_link(3, 0)

    s = camelot.read_pdf(link)

    df = s[0].df
    df.columns = df.iloc[0]
    df = df.drop(0)
    df = df.reset_index(drop=True)

    print(df.info())
    column_index = df.columns.get_loc(group)

    subjects_info = []

    for i in range(1, 5):
        main_string = df[df.columns[column_index]].iloc[i] 
        general_info = main_string.split('\n')

        index = main_string.rfind('\n')
        subject = main_string[:index].replace('\n','')

        if(subject=='ПРАКТИК'):
            subjects_info.append('К сожалению расписание на практику я не умею отпралять, его следует уточнить у преподавателя')
            break

        if('Разговоры' in subject):
            subject += 'важном"'
            subjects_info.append(f'Пара № {i}: {subject}')
        else:
            teacher = general_info[len(general_info)-1]         
            classroom = df.iloc[:,column_index+1].tolist()[i]
            subjects_info.append(f'Пара № {i} - {subject}\
                \nПреподаватель: {teacher}\
                \nКабинет: {classroom}')

    return subjects_info


get_today_schedule('')