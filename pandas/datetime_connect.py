import numpy as np
import pandas as pd
from tqdm import tqdm
import datetime

#두 개의 데이터 프레임(df_modify,이 있고 Time Variable이 존재할 때 가까운 시간끼리 연결하는 쿼리

df_modify_null = pd.DataFrame() #데이터 프레임을 만든다
for p_id in tqdm(afib['patient_id'].unique()): #patent_id 별로 반복문
    
    x = df_modify[df_modify['patient_id']==p_id].sort_values(by=['time'],ascending=False) #수정해야 할 DataFrame x 생성
    x.reset_index(drop=True,inplace=True)
    
    y = afib_null[afib_null['patient_id']==p_id].sort_values(by=['time'],ascending=False) #참고할 DataFrame y 생성
    y.reset_index(drop=True,inplace=True)
    
    if((len(x) != len(y))): #길이가 다르면 일일히 하나씩 시간 대조해 봐야 함
        for i in range(len(x)): 
            for j in range(len(y)):
                if(x.iloc[i]['time'] >= y.iloc[j]['time']): #x가 이후 시간이면
                    if(x.iloc[i]['time'] - y.iloc[j]['time'] < datetime.timedelta(seconds=600)): #600초 이내에 해당하면
                        x.loc[i,'Doctor_Dx'] = y.loc[j,'Doctor_Dx'] #참고할 DataFrame 진단 값을 수정할 DataFrame 진단 값에 넣는다
                        x.loc[i,'time2'] = y.loc[j,'time']
                else: #y가 이후 시간이면
                    if(y.iloc[j]['time'] - x.iloc[i]['time'] < datetime.timedelta(seconds=600)):
                        x.loc[i,'Doctor_Dx'] = y.loc[j,'Doctor_Dx']
                        x.loc[i,'time2'] = y.loc[j,'time']
        df_modify_null = df_modify_null.append(x)
    else:
        pass
        
        
    #번외
    df_modify_null_check = df_modify_null[~df_modify_null['time2'].isnull()] #중복되는 데이터는 안전하게 그냥 보존
    
    
