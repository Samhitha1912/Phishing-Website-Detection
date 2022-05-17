from flask import Flask, jsonify
from flask import request
import time
import json
from flask_cors import CORS
import joblib
import streamlit as st
import pandas as pd 

app = Flask(__name__)

cors = CORS(app, resources={r"*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/predict", methods=['GET'])
def hello_world():

  loaded_model = joblib.load('model.pkl')
  result = loaded_model.predict([[1,1,-1,1,-1,1,-1,-1,1,-1,1,-1,-1,-1,1,-1,1,-1,1,-1,-1,-1,1,1,-1,1,-1,1,-1,-1,-1]])
  
  for r in result:
    if r == 0:
      return jsonify({"result": "Not Phishing"})
    else:
      return jsonify({"result": "Phishing"})