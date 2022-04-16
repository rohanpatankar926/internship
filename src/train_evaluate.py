
from genericpath import exists
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
import os
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
    learning_rate=config["estimators"]["GradientBoostingRegressor"]["params"]["learning_rate"]
    n_estimators=config["estimators"]["GradientBoostingRegressor"]["params"]["n_estimators"]
    alpha=config["estimators"]["GradientBoostingRegressor"]["params"]["alpha"]
    verbose=config["estimators"]["GradientBoostingRegressor"]["params"]["verbose"]
    val_factor=config["estimators"]["GradientBoostingRegressor"]["params"]["validation_fraction"]
    tol=config["estimators"]["GradientBoostingRegressor"]["params"]["tol"]
    ccp_alpha=config["estimators"]["GradientBoostingRegressor"]["params"]["ccp_alpha"]
    x_train,x_test=train.drop(target_col,axis=1),test.drop(target_col,axis=1)
    
    y_train,y_test=train[target_col],test[target_col]
    
    GB=GradientBoostingRegressor(learning_rate=learning_rate,n_estimators=n_estimators,alpha=alpha,verbose=verbose,validation_fraction=val_factor,tol=tol,ccp_alpha=ccp_alpha)
    GB.fit(x_train,y_train)
    y_pred=GB.predict(x_test)
    
    (r2,rmse,mae,mse)=eval_metrics(y_test,y_pred)
    print(r2*100,rmse,mae,mse)
    
    normalized_rmse=rmse/(63770.43-1121)
    print(f"normalized rmse::{normalized_rmse}")
    
    os.makedirs(model_dir,exist_ok=True)
    model_path=os.path.join(model_dir,"model.pkl")
    
    joblib.dump(GB,model_path)
    
#################reports logging###############

    scores_file=config["reports"]["scores"]
    params_file=config["reports"]["params"]
    
    with open(scores_file,"w") as f:
        scores={
           "rmse":rmse,
           "mse":mse,
           "r2 score":r2,
           "rmse":rmse,
           "normalized rmse":normalized_rmse
            }
        json.dump(scores,f,indent=4)
    with open(params_file,"w") as f:
        params={
            "learning_rate":learning_rate,
            "n_estimators":n_estimators,
            "verbose":verbose,
            "validation_fraction":val_factor,
            "tol":tol,
            "ccp":ccp_alpha
        }
        json.dump(params,f,indent=4)

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    model_eval(config_path=parsed_args.config)
