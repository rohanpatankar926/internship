#split raw data
#save it in data/procesd data

import os 
import argparse
from sklearn.model_selection import train_test_split
from get_data import read_params
import pandas as pd

def train_test_split_(config_path):
    config=read_params(config_path)
    raw_data_path=config["load_data"]["raw_data_csv"]
    train_data=config["split_data"]["train_path"]
    test_data=config["split_data"]["test_path"]
    split_ratio=config["split_data"]["split_ratio"]
    random_state=config["base"]["random_state"]
    
    data=pd.read_csv(raw_data_path,sep=",")
    train,test=train_test_split(data,test_size=split_ratio,random_state=random_state)
    train.to_csv(train_data,sep=",",index=False,encoding="UTF-8")
    test.to_csv(test_data,sep=",",index=False,encoding="UTF-8")
    train_data=pd.read_csv(train_data)
    print(train_data)
    test_data=pd.read_csv(test_data)
    print(test_data)
    print(test_data.shape)
    print(train_data.shape)
    
if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args=args.parse_args()
    data=train_test_split_(config_path=parsed_args.config)