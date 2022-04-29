# 모든 column이 Null값일 때 삭제
data.dropna(how='all')
# 하나라도 column이 Null값일 때 삭제
data.dropna(how='any')
# 2개 이상의 column이 Null값일 때 삭제
data.dropna(thresh=2)
# 특정 column이 null 값일 때 삭제
data.dropna(subset = ['special'])

# Return Missing Value's index
df['주소'][df['주소'].isnull()]
