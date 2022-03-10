print('P_width_mean : ',np.nanmean(waves_cwt['ECG_P_width']))
print('P_width_median : ',np.nanmedian(waves_cwt['ECG_P_width']))
print('P_width_std : ',np.nanstd(waves_cwt['ECG_P_width']))
print('P_width_min : ',np.nanmin(waves_cwt['ECG_P_width']))
print('P_width_max : ',np.nanmax(waves_cwt['ECG_P_width']))

# Nan 값을 무시하고 기초 통계량 계산
