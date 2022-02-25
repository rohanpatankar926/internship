import os
import argparse
from get_data import read_params,get_data

def load_data(config_path):
    config=read_params(config_path)
    data=get_data(config_path)
    raw_data=config["load_data"]["raw_data_csv"]
    data.to_csv(raw_data,sep=",",index=False)

if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args=args.parse_args()
    load_data(config_path=parsed_args.config)