from distutils.command.config import config
from urllib import response
from flask import Flask,render_template,jsonify,request
import os
import joblib
import numpy as np
import yaml
import pandas as pd
import logging
logging.basicConfig(format='%(message)s',level=logging.INFO)

params_path="params.yaml"
webapp_root="webapp"
static_dir=os.path.join(webapp_root,"static")
template_dir=os.path.join(webapp_root,"templates")

logging.info("folder linking successful")

app=Flask(__name__,static_folder=static_dir,template_folder=template_dir)

def read_params(config_path):
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
    return config

logging.info("parmas.yaml read successful...")

def predict(data):
    config=read_params(params_path)
    model_dir_path=config["webapp_model_dir"]
    model=joblib.load(model_dir_path)
    prediction=model.predict(data)
    print(prediction)
    return prediction


def api_response(request):
    try:
        data=np.array([list(request.json.values())])
        response=predict(data)
        response={"response":response}
        return jsonify(response)
    except Exception as e:
        print(e)
        error={"something went wrong try again!!"}
        return error

config=read_params(params_path)
raw_data=config["raw_data"]["raw"]
data1=pd.read_csv(raw_data)
print(data1.head())


logging.info("csv read successful")

@app.route("/",methods=["GET","POST"])
def index():
    sex=sorted(data1["sex"].unique())
    smoker=sorted(data1["smoker"].unique())
    region=sorted(data1["region"].unique())
    if request.method=="POST":
        try: 
            if request.form:
                # data=dict(request.form)
                # data=[list(map(float,data))]
                # response=predict(data)
                # return render_template("index.html",response=response)
                age=int(request.form.get("age"))
                sex=(request.form.get("sex"))
                if(sex=="female"):
                    sex=0
                else:
                    sex=1
                bmi=float(request.form.get("bmi"))
                children=request.form.get("children")
                smoker=request.form.get("smoker")
                if(smoker=="no"):
                     smoker=0
                else:
                    smoker=1
                region=request.form.get("region")
                if region=="northeast":
                    region=0
                elif region=="northwest":
                    region=1
                elif region=="southeast":
                    region=2
                else:
                    region=3
                response=predict(pd.DataFrame([[age, sex, bmi, children, smoker, region]], columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region']))
                return render_template("index.html",response=str(response[0]))
            elif request.json:
                response=api_response(request)
                return jsonify(response)
        except Exception as e:
            print(e)
            error = {"error": "Something went wrong!! Try again later!"}
            error = {"error":e}
            return render_template("404.html", error=error)
    
    return render_template("index.html",sex=sex,smoker=smoker,region=region)

logging.info("application running succesfully")
if __name__=="__main__":
    app.run(debug=True)
    