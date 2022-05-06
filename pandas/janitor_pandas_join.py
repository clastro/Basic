from tqdm import tqdm
import pandas as pd
import janitor

#machine_results, doctor_results 는 이미 존재함
#doctor_results의 Study_Date 와 machine_results의 Study_Date_low,Study_Date_high 사이의 조건이면 Join 
# +-1시간으로 설정함

df_make_database = pd.DataFrame(columns=['PatientInfo.ID', 'PatientInfo.EncodedPatientID', 'StudyInfo.Date',\
       'StudyInfo.Time', 'ECGMeasurements.Severity', 'Diagnosis', 'Dx'])
for encoded_id in tqdm(doctor_remain_results['EncodedID'].unique()):
    df_machine = machine_results[machine_results['PatientInfo.EncodedPatientID']==encoded_id].sort_values(ascending=True,by=['StudyInfo.Date'])
    df_doctor = doctor_results[doctor_results['EncodedID']==encoded_id].sort_values(ascending=True,by=['Study_Date'])
    df_machine['Study_Date_low'] = df_machine['Study_Date'] - datetime.timedelta(hours=1) # 1시간 이전
    df_machine['Study_Date_high'] = df_machine['Study_Date'] + datetime.timedelta(hours=1) # 1시간 이후
    df_machine.reset_index(drop=True,inplace=True)
    df_doctor.reset_index(drop=True,inplace=True)
    
    if(len(df_machine) != len(df_doctor)):
        df_doctor.reset_index(drop=True,inplace=True)
        df_machine.reset_index(drop=True,inplace=True)
        df_join = df_doctor.conditional_join(df_machine, 
                           ('Study_Date', 'Study_Date_low', '>='), 
                           ('Study_Date', 'Study_Date_high', '<=')
                          )
        df_label = df_join['right']
        df_label['Dx'] = df_join['left']['Dx']
        df_label.drop(['Study_Date','Study_Date_low','Study_Date_high'],1,inplace=True)

    else:
        continue
    df_make_database = df_make_database.append(df_label)
        
