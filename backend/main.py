#Customize Created Functions
from upload.upload import parsefile
from dataframe.token import corpus
from dataframe.TXTtoCSV import dataframe
from dataframe.preprocessing import preProcess
from dataframe.insights import insights
from dummy.test import tempory
from JSON.wordcloud import WordCloudfun
 
import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app, prefix="/api/v1/dummy")
auth = HTTPBasicAuth()
app.config["DEBUG"] = True

#Add bearer token for authentication
cors = CORS(app, resources={r"*": {"origins": "*"}})


@app.route('/', methods=['GET'])
def hello():
    return "pong"

#Testing Route
@app.route('/testing', methods=['GET'])
def index():
    CORPUS = []
    df = pd.DataFrame()
    path="C:/Users/yashd/Downloads/WhatsApp Chat with Sumit Skn.txt"
    content=parsefile(path)
    # print(content[6])
    content=corpus(content)
    content=preProcess(content)
    
    """     SAVING DATA IN content VARIABLE      """

    
    """IMPORTANT LINES FOR TESTING"""
    # print(len(content))
    # print(content[32])
    #for i in range(len(content)):
    #print(content[1])
    df = dataframe(content)
    insights(df)
    #print(df)
    df.to_csv('dummy.csv')
    return "ping"

#API Route
@app.route('/api/v1/dummy', methods=['GET'])
def api():
    books = tempory()
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)