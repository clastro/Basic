import pandas as pd
import numpy as np
import psutil
import ray #ray library import

num_cpus = psutil.cpu_count(logical=False) #가능한 CPU 숫자 불러오기

ray.init(num_cpus=num_cpus) #ray 초기화

@ray.remote
def find_peak(df_unique_id):
  result = df_unique_id
  return result

futures = [find_peak.remote(unique_id_dict[i]) for i in range(num_cpus)] #remote 이하 함수를 실행하는 프로세스들을 futures에 담는다

results = ray.get(futures) #결과는 ray.get으로 동시에 받음
