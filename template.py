import os 


dirs=[
    
    os.path.join("data","raw"),
    os.path.join("data","processed"),
    "notebooks files",
    "saved_models",
    "src"
]

for dir in dirs:
    os.makedirs(dir,exist_ok=True)
    with open(os.path.join(dir,".gitkeep"),"w") as f:
        pass

files=[
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py")
]

for file in files:
    with open(file,"w") as f:
        pass