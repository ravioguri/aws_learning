from flask import Flask
import boto3

app = Flask(__name__)

@app.route("/home")
def homepage():
    return "AWS Assignment experiments lol"


@app.route("/")
def app_s3():
    
    client = boto3.client('s3')
    response = client.list_buckets()

    buckets=[]
    for bucket in response['Buckets']:
        buckets.append(bucket["Name"])

    for i in buckets:
        print(i)

        echo = client.list_objects(Bucket=i)

        bucketfiles = []

        for i in range(len(echo['Contents'])):
            bucketfiles.append(echo.get('Contents', [])[i]['Key'])
            print(bucketfiles[i])
    
    listToStr = ' '.join([str(elem) for elem in bucketfiles])
    return listToStr


'''@app.route("/home/<folder_name>")
def home():
    s3_obj = boto3.resource('s3')'''
    
