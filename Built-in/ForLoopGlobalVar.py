#반복문으로 변수 생성하기

try:
    globals()['P_Offsets_'+str(i)] = waves_cwt['ECG_P_Offsets'][i-1]
except:
    globals()['P_Offsets_'+str(i)] = ''
