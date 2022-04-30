## INSURANCE PREMIUM PREDICTION USING MLOPS

### Problem Statement:<br>
The goal of this project is to give people an estimate of how much they need based on their individual health situation. After that, customers can work with any health insurance carrier and its plans and perks while keeping the projected cost from our study in mind. This can assist a person in concentrating on the health side of an
insurance policy rather han the ineffective part.

### Approach: <br>
The classical machine learning tasks like Data Exploration, Data Cleaning,
Feature Engineering, Model Building and Model Testing. Try out different machine
learning algorithms that’s best fit for the above case.
Some Famous Algorithms: - Multiple Linear Regression, Decision tree Regression and
Gradient Boosting, Decision tree, Regression

### Results: <br>
We have to build a solution that should able to predict the premium of the
personal for health insurance

DEPLOYED APPLICATION LINK:https://mlops-application.herokuapp.com/<br>
<br>
FOR DOCUMENTATION OF THIS PROJECT VISIT HERE:[DOCS](https://github.com/rohanpatankar926/internship_project/tree/main/docs)
<br>
### STEPS ARE MENTIONED BELOW FOR MAKING THE ENTIRE PIPELINE
step1 :
``` bash
conda create -n filename python=3.7
```
step2 :
Create ```template.py``` file and create files and directories


step 3:
Inside the ```params.yaml``` file understand it and append the code i have written <br>
Also same for ```dvc.yaml```<br>
These 2 are the brain and heart for this mlops dvc project<br>

step 4:<br> 
Inside the ```src``` dir create ```get_data.py```<br>
OR<br>
```touch src/get_data.py```<br>
The main objective for making this file is to get track of params.yaml file and to read the data present in our local system.If you want to read data from s3 bucket or azure you can also customize the code and fetch the data<br>

step 5:<br>
After step 5 open up vscode or pycharm terminal<br>
Follow these commands<br>
1.```pip install -r requirements.txt```<br>
2.```git init```<br>
3.```dvc init```<br>
4.```dvc add data_given/csv_file_name.csv```<br>
5.```git add .```<br>
6.```git commit -m "committed"```<br>
7.```git remote add origin git repo https address```<br>
8.```git branch -M main```<br>
9.```git push origin main```<br>

step 6:<br>
Inside the ```src``` dir create ```load_data.py``` file<br>
OR<br>
```touch src/load_data.py```<br>
The main objective for this file is we will write a ```function``` which will fetch ```.csv``` file and append to ```raw``` data folder.<br>

step 7:<br>
Inside the ```src``` dir create ```split_data.py```<br>
OR <br>
```touch src/split_data.py```<br>
The main objective for this file by the ```sklearn``` library we will divide the data into ```75:25``` ratio and then append to ```processed``` folder <br>

step 8:<br>
Inside the ```src``` dir create ```train_evaluate.py```<br>
OR<br>
```touch src/train_evaluate.py```<br>
This is the favorite step for all data science enthusiasts we will train and evaluate the model here.<br>

step 9:<br>
After evaluating the model i got around **85%** accuracy of r2 score and around **0.07** normalized rmse score formula for **r2=1-rss/tss** and rmse formuala **np.sqrt((x-x^)^2)/n** and normalized rmse formula **rmse/max-min of the target**.Save and dump it to **saved_models** directory.

step 10:<br>
Come to terminal and follow these commands
```dvc repro```
```dvc params diff``` if not worked try below one
```dvc metrics show``` 
This will track all the scores,parameters of ml algorithm and in future if u changed any ml algorithm it will track and show in logs.

step 11:<br>
Come to terminal and install few packages
```pip install pytest```
```pip install tox```
These packages are used for testing environment.



step12:<br>
create file named ```tox.ini``` it is used bcz tox is a generic virtualenv management and test command tool that is used for.
-->>Helps in running your tests in each environment.
schema
```bash        
[tox]
    envlist=py37
    [testenv]
    deps=pytest
    command=pytest -v
```

step 13:<br>
make dir ```test``` inside test create files ```__init__.py```,```conftest.py```,```test_config.py```
These files help us for testing environment.

step 14:<br>
come to terminal 
```pytest -v``` type it will test and give test cases pass or fail

step 15:
create ```setup.py``` in root dir it is help us to create python package.
Come to terminal 
Type ```tox``` 
it will install all the dependencies if no error it will pass the test cases otherwise it will give error.

step 16:
```name="src"``` and create package of our model
Come to terminal 
```python setup.py sdist bdist_wheel``` it will create ```.tar``` file and create package ```src```

step 17:
All our procedure fininshed
Now time to create webapp
```bash
├───static
│   └───css
│           main.css
│
└───templates
        404.html
        base.html
        index.html
```
step 18:
```app.py``` on root dir for creating flask api
Now make routes like `\` for rendering home page and `/predict` for rendering predictions and extra `predict_postman` you can add here for testing in postman which is `jsonify` it will give json results

step 19:
create package for this project so that new user can install our package and can use this project <br>
visit here : https://packaging.python.org/en/latest/tutorials/packaging-projects/

step 20:
For automation of the project create dir `.github\workflow\ci-cd.yaml` we used here github actions for automating our project 


### Cloning this project 
`git clone https://github.com/rohanpatankar926/internship_project.git`<br>
`cd project directory`
`pip install -r requirements.txt`
`python app.py`<br>
All set now you cloned this project successfully
<br>
Author:Rohan patankar
<br>
For any queries related to ml/dl contact me <a href="mailto:rohanpatankar926@gmail.com?subject = Feedback&body = Message">rohanpatankar926@gmail.com</a>
<br>
### Thank You
