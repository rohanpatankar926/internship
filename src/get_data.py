#The main objective for this code is it will read params.yaml process it and return to a dataframe


import os #handling file 
import argparse #for argument parsing
import yaml #yaml file calling
import pandas as pd #dataframe calling

def read_params(config_path):
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
    return config

def get_data(config_path):
    config=read_params(config_path)
    print(config)
    data_path=config["data_source"]["local_data"]
    raw_path=config["raw_data"]["raw"]
    data=pd.read_csv(data_path,sep=",")
    raw_data=pd.read_csv(raw_path,sep=",")
    print(raw_data.head())
    return data


if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args=args.parse_args()
    data=get_data(config_path=parsed_args.config)