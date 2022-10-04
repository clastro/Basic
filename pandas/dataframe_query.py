#데이터프레임 내 multi columns에 대한 isin 함수가 필요할 때 (query를 사용)

query = '(main_cate1 in @train_category) & (sub_cate1_1 in @train_category2) & (sub_cate2_1 in @train_category2) &' +\
'(main_cate2 in @train_category2) & (sub_cate1_2 in @train_category2) & (sub_cate2_2 in @train_category2) &' +\
'(main_cate3 in @train_category2) & (sub_cate1_3 in @train_category2) & (sub_cate2_3 in @train_category2)'   

df.query(query)

#DF1 rows - DF2 rows

DF=DF1[~DF1.isin(DF2)].dropna(how = 'all')
