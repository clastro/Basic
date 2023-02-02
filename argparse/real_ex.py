import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from tsfresh import extract_features
from sklearn.utils import shuffle
from tqdm import tqdm
from DBhandle import DBconn
from sqlalchemy import create_engine
import sys
import argparse

engine = create_engine('x.db', echo=False)

parser = argparse.ArgumentParser()

parser.add_argument('--label', default=0, type=int)
parser.add_argument('--split_data', default='train', type=str)

args = parser.parse_args()

def numpy_load(filename):
    ecg = np.load(filename)
    return ecg

def make_dataset(files,label):
    
    label_dict = {0:'n',1:'s',2:'v',3:'p',4:'q',5:'e'}
    
    n = min(10000,len(files))
    
    for filename in tqdm(files[:n]):
        
        ecg = numpy_load(filename)
        df = pd.DataFrame(columns=['id','time','ecg'])
        df['ecg'] = ecg
        df['id'] = label
        df['time'] = [*range(len(df))]
        extracted_features = extract_features(df, column_id="id", column_sort="time")
        df_dataset = extracted_features.reset_index()
        df_dataset.to_sql('beat_'+label_dict[label]+'_'+args.split_data, con=engine, if_exists='append',index=False)

path = '/beats3/'
print(args)
files = glob.glob(path+args.split_data+'*_'+str(args.label)+'.npy')

shuffle_files = shuffle(files,random_state=0)
make_dataset(shuffle_files,args.label)

