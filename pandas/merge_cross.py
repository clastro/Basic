# 28분 Query

normal_ecg_afib_days = pd.DataFrame()
for afib_id in tqdm(afib_patients_id):
    AFib_date_list = [date for date in df_Afib_patients[df_Afib_patients['patient_id']==afib_id]['date']] #환자의 AFib 걸린 날 리스트
    x = df_normal_ecg_by_Afib[df_normal_ecg_by_Afib['patient_id']==afib_id] #같은 환자의 Normal 리스트
    warnings.filterwarnings("ignore") #오류 메세지 무시
    if(len(x)>0): #Normal 리스트가 존재한다면
        for date in AFib_date_list:
            #x['difference'] = x['date'].apply(lambda x : date - x).dt.days
            x['difference'] =  date - x['date']
            x_transform = x[(x['difference'].dt.days>= from_days)&(x['difference'].dt.days<= to_days) ]
            normal_ecg_afib_days = pd.concat([normal_ecg_afib_days,x_transform],axis='rows')
    else:
        continue
        
# 21분 Query

normal_ecg_afib_days = pd.DataFrame()
for afib_id in tqdm(afib_patients_id):
    x = df_Afib_patients_ecg[df_Afib_patients_ecg['patient_id']==afib_id]
    
    res = (pd.merge(x[['date','unique_id','tag']].reset_index(), x[['date','unique_id','tag']].reset_index(), how='cross')
         .query('index_x < index_y')
         .drop(columns=['index_x', 'index_y']))
    res['diff'] = (res['date_x'] - res['date_y']).dt.days
    
    y = res[(res['tag_x']=='afib') & (res['tag_y']=='normal') & ((res['diff']< to_days) & (res['diff']> from_days))]
    normal_ecg_afib_days = pd.concat([normal_ecg_afib_days,y],axis='rows')
