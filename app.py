from flask import Flask
import boto3
from flask import render_template

app = Flask(__name__)

@app.route("/home")
def homepage():
    return "AWS Assignment experiments lol"


@app.route("/")
def app_s3():
    
    client = boto3.client('s3')
    response = client.list_buckets()

    buckets=[]
    names = dict()
    for bucket in response['Buckets']:
        buckets.append(bucket["Name"])

    for i in buckets:
        print(i)

        echo = client.list_objects(Bucket=i)

        bucketfiles = []

        for j in range(len(echo['Contents'])):
            bucketfiles.append(echo.get('Contents', [])[j]['Key'])
            print(bucketfiles[j])
        names[i] = bucketfiles

    #listToStr = ' '.join([str(elem) for elem in bucketfiles])
    return render_template('home.html',allfiles=names)


    
