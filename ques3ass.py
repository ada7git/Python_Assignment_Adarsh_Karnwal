from flask import Flask, request
from pymongo import MongoClient                                                    

app = Flask(__name__)                                                                      

client = MongoClient('mongodb://localhost:3307/')
db = client['demo']
collection = db['config']

@app.route('/config', methods=['GET']) 
def read(): 
    try:
        with open("SampleConfig.txt") as data:
            list = data.readlines()
            list = [item.replace("\n","").replace(" ","").replace('"',"") for item in list]
            json={}
            key=""
            di={}
            print(list)
            for item in list:
                 last = item[-1:]
                 if (last==":"):
                      if (len(str(di))!=0):
                           json[key]=di
                           key = item[0:-1]
                           di={}
                 else:
                    innerLoop = item.split(":")
                    di[innerLoop[0]]= innerLoop[1]
            json[key]=di
            del json[""]
            collection.insert_one(json) 
        return "Congratulations! Data is added"
    except Exception:
         return str(Exception.__init__)
    

if __name__ == '__main__': 
	app.run(port=8080) 

read()

