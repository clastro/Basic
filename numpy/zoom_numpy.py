for i,uid in tqdm(zip(pred[0],ECG_Sample['unique_id'])):
    convert_i = scipy.ndimage.zoom(
  i[250:], (25/11, 1))
    np.save('/smc_work/datanvme/smc/vae/'+uid,convert_i)
    
    
# zoom 명령어를 통해 image array 늘리기, 가로 크기 약 2.5배
