import pandas as pd

#Column 이름 변경

df_afib.rename(columns = {'start_date' : 'incidence_date'}, inplace = True)
#start_date를 incidence_date로 바꿈

df_afib['start_date'] = pd.to_datetime(df_afib['start_date'])
#start_date의 데이터 타입을 datetime으로 변경 (format에 맞아야 변경이 가능함)
