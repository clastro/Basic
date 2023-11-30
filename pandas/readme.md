### DataFrame의 2개 칼럼을 비교해서 빈 값을 채워 넣는 방법

```
A['col1'].fillna(B['col1'], inplace=True)
A['col2'].fillna(A['col1'], inplace=True)
```
### 문자열 데이터 칼럼을 숫자로 변환하는 방법

```
df_data_group['patient_id'].astype('category').cat.codes
```

### 시간 계산하기 (timedelta)

```
df_afib_in_afib[df_afib_in_afib['patient_id'] == pid]['time'].min() - timedelta(days=365)
```

### 데이터프레임의 숫자 칼럼만 추출하여 차이 계산하기

```
df_diff = second_df.select_dtypes(include=['number']) - first_df.select_dtypes(include=['number'])
```
