# No.1

# apply lambda

df_only_normal_patients = df_patients_info.groupby('patient_id').apply(lambda x : x.Dx.str.contains('sinus rhythm',case=False).all() == True)
normal_patients_id = df_only_normal_patients[df_only_normal_patients == True].index.tolist()
len(normal_patients_id)
# 4분 소요

# vectorization

nsr_check = df_patients_info['Dx'].str.contains('sinus rhythm',case=False)
df_only_normal_patients = nsr_check.groupby(df_patients_info['patient_id'],sort=False).all() == True
df_only_normal_patients[df_only_normal_patients == True]

# CPU times: user 19 µs, sys: 0 ns, total: 19 µs
# Wall time: 32.7 µs
