# ecg_wave : (5000,12) 2D-array
#np.pad(array, pad_width, mode='constant')

if ecg_wave.shape[0] < 5040:
    padding_needed = 5040 - ecg_wave.shape[0]
    ecg_wave_padded = np.pad(ecg_wave, ((0, padding_needed), (0, 0)), mode='constant') # 행에 대해서 padding을 추가함, 열에 대해서는 padding을 추가하지 않음
elif ecg_wave.shape[0] > 5040:
    # ECG 데이터가 5040보다 크면 자르기
    ecg_wave_padded = ecg_wave[:5040, :]
