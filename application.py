from flask import Flask,jsonify,request,render_template
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

ridge = pickle.load(open('pickle/ridgecv.pkl','rb'))
scalar = pickle.load(open('pickle/scalar.pkl','rb'))

application= Flask(__name__)
app = application
@app.route("/")
def welcome():
    return render_template("home.html")

@app.route("/predict",methods=['GET','POST'])
def predict():
    if request.method=='POST':
        # month = request.form.get("month")
        # day = request.form.get("day")
        # year = request.form.get("year")
        temperature = request.form.get("Temperature")
        rh = request.form.get("RH")
        ws = request.form.get("Ws")
        rain = request.form.get("Rain")
        ffmc = request.form.get("FFMC")
        dmc = request.form.get("DMC")
        isi = request.form.get("ISI")
        # fwi = request.form.get("FWI")
        classes = request.form.get("Classes")
        region = request.form.get("Region")
        
        input=[[temperature,rh,ws,rain,ffmc,dmc,isi,classes,region]]
        input = scalar.transform(input)
        predict = ridge.predict(input)
        return render_template('predict.html',predict=predict[0])
    else:
        return render_template("predict.html")
if __name__=="__main__":
    app.run(debug=True)
    