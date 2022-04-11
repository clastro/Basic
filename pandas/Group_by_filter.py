#Groupby된 해당 칼럼의 조건을 조회
df_patient_info.groupby('patient_id').filter(lambda x : x.gender.str.contains('Unknown',case=False).all()== True)
