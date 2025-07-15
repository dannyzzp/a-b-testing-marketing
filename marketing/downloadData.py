import os
import subprocess
import zipfile

destinationFolder = "/home/dannyzzp/projects/marketing/data/raw"
if not (os.path.exists(os.path.join(destinationFolder, 'marketing_AB.csv'))):
    try:
        ''' Run curl command and download kaggle dataset
        '''
        result = subprocess.run(
            ["curl", "-L", '-o', destinationFolder+"/marketing-ab-testing.zip", "https://www.kaggle.com/api/v1/datasets/download/faviovaz/marketing-ab-testing"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        with zipfile.ZipFile(destinationFolder+'/marketing-ab-testing.zip', 'r') as zip_ref:
            zip_ref.extractall(destinationFolder)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
else:
    print(f"marketing_AB.csv already exists in {destinationFolder}")