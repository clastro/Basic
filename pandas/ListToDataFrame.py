# 크기가 같은 리스트들의 데이터프레임 변환


#Dictionary를 사용하는 방법

insert_df = pd.DataFrame(
    {'video_id': id_lists,
     'channel_id': channel_lists,
     'views': view_lists,
     'date' : day_lists
    })

#Columns에 직접 넣는 방법

insert_df = pd.DataFrame(id_lists,columns=['video_id'])
insert_df['channel_id'] = channel_lists
insert_df['views'] = view_lists
insert_df['date'] = day_lists
