import pandas as pd

# Читаем исходный CSV файл
df = pd.read_csv('backend_logic/schedules/course_1.csv')

# Создаем пустой DataFrame для нового расписания
new_df = pd.DataFrame()

# Проходим по всем группам (колонкам) в исходном DataFrame
for group in df.columns:
    # Проходим по всем строкам для текущей группы
    for i in range(len(df)):
        # Получаем значение ячейки (предмет и преподаватель)
        cell_value = df.loc[i, group]
        
        # Пропускаем пустые значения
        if pd.isna(cell_value):
            continue
            
        # Разделяем предмет и преподавателя (предполагаем формат "Предмет (Преподаватель)")
        if '(' in cell_value and ')' in cell_value:
            subject = cell_value.split('(')[0].strip()
            teacher = cell_value.split('(')[1].replace(')', '').strip()
            
            # Определяем номер пары и день
            # (предполагаем, что 5 пар в день, всего 5 дней)
            day = i // 5 + 1
            lesson_number = i % 5 + 1
            
            # Создаем уникальный идентификатор для пары (день + номер пары)
            lesson_id = f"День {day}, Пара {lesson_number}"
            
            # Добавляем запись в новый DataFrame
            if teacher not in new_df.columns:
                new_df[teacher] = pd.Series(dtype='object')
                
            new_df.at[lesson_id, teacher] = subject

# Сортируем строки по дням и номерам пар
new_df = new_df.sort_index()

# Сохраняем результат в новый CSV файл
print('done')
new_df.to_csv('расписание_преподаватели.csv')