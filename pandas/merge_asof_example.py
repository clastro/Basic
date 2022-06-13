#merge_asof_example
#2개의 DataFrame A와 B의 key가 기간이면서 그 기간이 완벽히 일치하지 않고 비슷한 경우에 Join 하는 방법

import numpy as np
import pandas as pd
from tqdm import tqdm
import datetime


ray.init(num_cpus=num_cpus) #Multiprocessing을 위한 ray 초기화

batch = int(patient_id_array.shape[0]/num_cpus) + 1 #batch 단위 쪼개기

patient_id_dict = {}
start = 0
for i in range(num_cpus):
    patient_id_dict[i] = patient_id_array[start:start+batch]
    start += batch

@ray.remote
def function_Dx(df_x,df_y,patient_id_list): #df_x와 #df_y의 기간을 비교해서 합치기
    
    df_total = pd.DataFrame()
    
    for patient_id in tqdm(patient_id_list):
    
        x = df_x[df_x['patient_id']==patient_id].sort_values('Study_Date')
        x.reset_index(drop=True,inplace=True)
        y = df_y[df_y['ID']==patient_id].sort_values('Study_Date')
        y.reset_index(drop=True,inplace=True)
        
        try:

            test = pd.merge_asof(x[['Study_Date','unique_id','Dx','patient_id']].sort_values(by=['Study_Date'])\
                                 ,y[['Study_Date','Dx']].sort_values(by=['Study_Date']),\
                                 on='Study_Date',\
                                 allow_exact_matches=True,\
                                 tolerance=pd.Timedelta('1440 minute'),\ # Study Date가 24시간 이내
                                 direction='nearest') # 24시간 전후 - forward, backward Option 있음
            
        except:
            test = pd.merge_asof(x[['Study_Date','unique_id','Dx','patient_id']].sort_values(by=['Study_Date'])\
                                 ,y.dropna()[['Study_Date','Dx']].sort_values(by=['Study_Date'])\
                                 ,on='Study_Date'\
                                 ,allow_exact_matches=True,\
                                 tolerance=pd.Timedelta('1440 minute'),\
                                 direction='nearest')
            
        df_total = pd.concat([df_total,test],axis='rows')
    
    return df_total
  
futures = [function_Dx.remote(df_1,df_2,patient_id_dict[i]) for i in range(num_cpus)]
results = ray.get(futures)

df_data_2 = pd.DataFrame()
for i in range(len(results)):
    df = pd.DataFrame.from_dict(results[i]).drop_duplicates()
    df_data_2 = pd.concat([df_data_2,df])
