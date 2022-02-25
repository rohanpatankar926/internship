
import numpy as np
from sklearn.metrics import mean_absolute_error,r2_score,mean_squared_error
from sklearn.ensemble import GradientBoostingRegressor
from urllib.parse import urlparse
import pandas as pd
import argparse

from sklearn.model_selection import learning_curve
from get_data import read_params
import joblib
import json

def eval_metrics(act,pred):
    r2score=r2_score(act,pred)
    rmse=np.sqrt(mean_squared_error(act,pred))
    mse=mean_squared_error(act,pred)
    mae=mean_absolute_error(act,pred)
    return r2score,rmse,mse,mae

def model_eval(config_path):
    config=read_params(config_path)
    test_data=config["split_data"]["test_path"]
    train_data=config["split_data"]["train_path"]
    model_dir=config["model_dirs"]
    
    target_col=config["base"]["target_data"]
    train=pd.read_csv(train_data,sep=",")
    test=pd.read_csv(test_data,sep=",")
    
    x_train,x_test=train.drop(target_col,axis=1),test.drop(target_col,axis=1)
    
    y_train,y_test=train[target_col],test[target_col]
    
    GB=GradientBoostingRegressor()
    GB.fit(x_train,y_train)
    y_pred=GB.predict(x_test)
    
    (rmse,mae,r2,mse)=eval_metrics(y_test,y_pred)
    print(rmse,mae,r2,mse)
    
    
if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    model_eval(config_path=parsed_args.config)
