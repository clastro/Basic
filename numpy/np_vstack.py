# array stack을 빠르게 적용하기
# 더 좋은 방법 있으면 찾기 2022-07-11

rhythm = np.zeros(5000)
rhythms = np.zeros(5000)
i = 0
for unique_id in tqdm(df_data['unique_id']):
    rhythm = vstack(rhythm,res[unique_id])
    i+=1
    if(i % 400 == 0):
        rhythm = np.delete(rhythm,0,0)
        rhythms = np.vstack((rhythms,rhythm))
        rhythm = np.zeros(5000)
rhythms = np.vstack((rhythms,rhythm))
