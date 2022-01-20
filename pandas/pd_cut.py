## 칼럼 내 구간을 나눠서 분석해야 할 때 유용함

### 1. Before pd.cut  

df_group_ads[(df_group_ads['subscribers']>=10000) & (df_group_ads['subscribers']<50000)].mean()
df_group_ads[(df_group_ads['subscribers']>=50000) & (df_group_ads['subscribers']<100000)].mean()
df_group_ads[(df_group_ads['subscribers']>=100000) & (df_group_ads['subscribers']<500000)].mean()
df_group_ads[(df_group_ads['subscribers']>=500000)].mean()

### 매번 결과도 따로 출력해야 하고 번거로움.

### 2. After pd.cut

bins = [10000,50000,100000,500000,max(columns_number)]
bins_label = ['1만 이상 5만 미만','5만 이상 10만 미만','10만 이상 50만 미만','50만 이상']
df_group_ads["level"] = pd.cut(df_group_ads["subscribers"], bins, right=False, labels=bins_label)
df_group_ads.groupby('level').mean()

### 한 번에 테이블 안에 다른 칼럼까지 출력이 됨.
