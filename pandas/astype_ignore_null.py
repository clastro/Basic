df['PAxis'] = df_smc_all2['PAxis'].str.extract('(\d+)', expand=False).astype('float').astype('Int64')
df['RAxis'] = df_smc_all2['RAxis'].str.extract('(\d+)', expand=False).astype('float').astype('Int64')
df['TAxis'] = df_smc_all2['TAxis'].str.extract('(\d+)', expand=False).astype('float').astype('Int64')
