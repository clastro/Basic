### DataFrame의 2개 칼럼을 비교해서 빈 값을 채워 넣는 방법

```
A['col1'].fillna(B['col1'], inplace=True)
A['col2'].fillna(A['col1'], inplace=True)
```
### 문자열 데이터 칼럼을 숫자로 변환하는 방법

```
df_data_group['patient_id'].astype('category').cat.codes
```
