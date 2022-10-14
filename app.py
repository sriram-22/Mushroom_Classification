from distutils.log import debug
import pickle
from flask import Flask, json,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app= Flask(__name__)
Project = pd.read_csv("https://raw.githubusercontent.com/sriram-22/Mushroom_Classification/main/mushrooms.csv")
model=pickle.load(open('rfmodel.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html') 

@app.route('/predict_api',methods=['POST'])

def predict_api():
    data=request.json['data']
    d = pd.DataFrame(columns=list(Project.columns)[1:])
    d.loc[len(d.index)] = list(data.values())
    output=model.predict(d)
    json_output = int(output)
    return jsonify(json_output)



if __name__=="__main__":
    app.run(debug=True)