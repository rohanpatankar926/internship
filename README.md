step1 :
``` bash
conda create -n filename python=3.7
```

step2 :

Create ```template.py``` file and schema to it as shown below

```
C:.
│   .dvcignore
│   .gitignore
│   dvc.lock
│   dvc.yaml
│   params.yaml
│   README.md
│   requirements.txt
│   template.py
│
├───.dist
├───.dvc
│   │   .gitignore
│   │   config
│   │
│   ├───cache
│   │   ├───d0
│   │   │       5e1ef49a0942b9cc633ffd353a4290
│   │   │
│   │   ├───fb
│   │   │       6ae626d107130aee686992d93a5347
│   │   │
│   │   └───runs
│   │       └───ed
│   │           └───ed03693f864fdce4c92bdab0c22b27b17b4067fb2e632dce435b5e502ca62162
│   │                   59a9ac9752a6f94613bde2e584f4910ae77178bbf44da9566cda9baa1da76363
│   │
│   └───tmp
│       │   lock
│       │   rwlock
│       │
│       ├───links
│       │       cache.db
│       │
│       └───md5s
│               cache.db
│
├───data
│   ├───processed
│   │       .gitkeep
│   │       test_insurance.csv
│   │       train_insurance.csv
│   │
│   └───raw
│           .gitignore
│           .gitkeep
│           insurance_updated.csv
│
├───data_given
│       .gitignore
│       insurance_updated.csv
│       insurance_updated.csv.dvc
│
├───notebooks files
│       .gitkeep
│
├───saved_models
│       .gitkeep
│
└───src
    │   .gitkeep
    │   get_data.py
    │   load_data.py
    │   split_data.py
    │   train_evaluate.py
    │   __init__.py
    │
    └───__pycache__
            get_data.cpython-37.pyc
```
step 4:
Inside the ```params.yaml``` file understand it and append the code i have written <br>
Also same for ```dvc.yaml```<br>
These 2 are the brain and heart for this mlops dvc project<br>

step 5:<br> 
Inside the ```src``` dir create ```get_data.py```<br>
OR<br>
```touch src/get_data.py```<br>
The main objective for making this file is to get track of params.yaml file and to read the data present in our local system.If you want to read data from s3 bucket or azure you can also customize the code and fetch the data<br>

step 6:<br>
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

step 7:<br>
Inside the ```src``` dir create ```load_data.py``` file<br>
OR<br>
```touch src/load_data.py```<br>
The main objective for this file is we will write a ```function``` which will fetch ```.csv``` file and append to ```raw``` data folder.<br>

step8 :<br>
Inside the ```src``` dir create ```split_data.py```<br>
OR <br>
```touch src/split_data.py```<br>
The main objective for this file by the ```sklearn``` library we will divide the data into ```75:25``` ratio and then append to ```processed``` folder <br>

step9 :<br>
Inside the ```src``` dir create ```train_evaluate.py```<br>
OR<br>
```touch src/train_evaluate.py```<br>
This is the favorite step for all data science enthusiasts we will train and evaluate the model here.<br>

step 10:<br>
After evaluating the model i got around **85%** accuracy of r2 score and around **0.07** normalized rmse score formula for **r2=1-rss/tss** and rmse formuala **np.sqrt((x-x^)^2)/n** and normalized rmse formula **rmse/max-min of the target**.Save and dump it to **saved_models** directory.

step11:<br>
Come to terminal and follow these commands
```dvc repro```
```dvc params diff``` if not worked try below one
```dvc metrics show``` 
This will track all the scores,parameters of ml algorithm and in future if u changed any ml algorithm it will track and show in logs.

step12:<br>
Come to terminal and install few packages
```pip install pytest```
```pip install tox```
These packages are used for testing environment.



step13:<br>
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

step13:<br>
make dir ```test``` inside test create files ```__init__.py```,```conftest.py```,```test_config.py```
These files help us for testing environment.

step14:<br>
come to terminal 
```pytest -v``` type it will test and give test cases pass or fail

step15:
create ```setup.py``` in root dir it is help us to create python package.
Come to terminal 
Type ```tox``` 
it will install all the dependencies if no error it will pass the test cases otherwise it will give error.

step16:
```name="src"``` and create package of our model
Come to terminal 
```python setup.py sdist bdist_wheel``` it will create ```.tar``` file and create package ```src```

step17:
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
```app.py``` on root dir for creating flask api
