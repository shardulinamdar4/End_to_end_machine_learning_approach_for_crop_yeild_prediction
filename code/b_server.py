import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
import pprint
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import cross_val_score
from sklearn import metrics
import pickle
from flask import Flask, request, jsonify

def predict_bareilly(num1, num2,num3,num4):
    output = {'output prediction for bareilly':0}
    x_input = np.array([num1, num2, num3, num4]).reshape(1,4)
    filename = 'bareilly.pkl' # model for bareilly
    m1 = pickle.load(open(filename, 'rb'))
    output['output prediction for bareilly (in Tons)'] = m1.predict(x_input)[0].item()
    print(output)
    return output
def predict_coimbatore(num1, num2,num3,num4):
    output = {'output prediction for coimbatore':0}
    x_input = np.array([num1, num2, num3, num4]).reshape(1,4)
    filename = 'coimbatore.pkl' # model for bareilly
    m1 = pickle.load(open(filename, 'rb'))
    output['output prediction for coimbatore (in Tons)'] = m1.predict(x_input)[0].item()
    print(output)
    return output
def predict_ghazipur(num1, num2,num3,num4):
    output = {'output prediction for ghazipur':0}
    x_input = np.array([num1, num2, num3, num4]).reshape(1,4)
    filename = 'ghazipur.pkl' # model for bareilly
    m1 = pickle.load(open(filename, 'rb'))
    output['output prediction for ghazipur (in Tons)'] = m1.predict(x_input)[0].item()
    print(output)
    return output
def predict_hassan(num1, num2,num3,num4):
    output = {'output prediction for hassan':0}
    x_input = np.array([num1, num2, num3, num4]).reshape(1,4)
    filename = 'hassan.pkl' # model for bareilly
    m1 = pickle.load(open(filename, 'rb'))
    output['output prediction for hassan(in Tons)'] = m1.predict(x_input)[0].item()
    print(output)
    return output
def predict_sindhudurg(num1, num2,num3,num4):
    output = {'output prediction for sindhudurg':0}
    x_input = np.array([num1, num2, num3, num4]).reshape(1,4)
    filename = 'sindhudurg.pkl' # model for bareilly
    m1 = pickle.load(open(filename, 'rb'))
    output['output prediction for sindhudurg (in Tons)'] = m1.predict(x_input)[0].item()
    print(output)
    return output


app = Flask(__name__)

@app.route('/')
def index():
    return " Welcome to Agriyantra Rice Yeild Prediction Server 1. enter the previous year crop yeild 2.Enter the area of your farm 3. Enter previous year rainfall 4. enter this year rainfll "   # welcome page

@app.route("/bareilly", methods=['GET'])
def bareilly():
    body = request.get_data()
    header = request.headers
    
    try:
        num1 = int(request.args['pC']) # Previous year crop yeild
        num2 = int(request.args['area']) # Area
        num3 = int(request.args['r1']) # last year rainfall
        num4 = int(request.args['r2']) # this rainfall
        
        if((num1!=None) and (num2!=None) and (num3!=None) and (num4!=None)):
           res = predict_bareilly(num1, num2,num3,num4) # call the predict_bareilly function
        else:
           res = {'success': False,
                 'message': 'input proper data'}
           
    except:
           res = {'success': False,
                 'message': 'unkonwn error'}
    
    return jsonify(res)
@app.route("/coimbatore", methods=['GET'])
def coimbatore():
    body = request.get_data()
    header = request.headers
    
    try:
        num1 = int(request.args['pC']) # Previous year crop yeild
        num2 = int(request.args['area']) # Area
        num3 = int(request.args['r1']) # last year rainfall
        num4 = int(request.args['r2']) # this year rainfall
        
        if((num1!=None) and (num2!=None) and (num3!=None) and (num4!=None)):
           res = predict_coimbatore(num1, num2,num3,num4) # call the predict_bareilly function
        else:
           res = {'success': False,
                 'message': 'input proper data'}
           
    except:
           res = {'success': False,
                 'message': 'unkonwn error'}
    
    return jsonify(res)
@app.route("/ghazipur", methods=['GET'])
def ghazipur():
    body = request.get_data()
    header = request.headers
    
    try:
        num1 = int(request.args['pC']) # Previous year crop yeild
        num2 = int(request.args['area']) # Area
        num3 = int(request.args['r1']) # last year rainfall
        num4 = int(request.args['r2']) # this year  rainfall
        
        if((num1!=None) and (num2!=None) and (num3!=None) and (num4!=None)):
           res = predict_ghazipur(num1, num2,num3,num4) # call the predict_bareilly function
        else:
           res = {'success': False,
                 'message': 'input proper data'}
           
    except:
           res = {'success': False,
                 'message': 'unkonwn error'}
    
    return jsonify(res)
@app.route("/hassan", methods=['GET'])
def hassan():
    body = request.get_data()
    header = request.headers
    
    try:
        num1 = int(request.args['pC']) # Previous year crop yeild
        num2 = int(request.args['area']) # Area
        num3 = int(request.args['r1']) # last year rainfall
        num4 = int(request.args['r2']) #this year  rainfall
        
        if((num1!=None) and (num2!=None) and (num3!=None) and (num4!=None)):
           res = predict_hassan(num1, num2,num3,num4) 
        else:
           res = {'success': False,
                 'message': 'input proper data'}
           
    except:
           res = {'success': False,
                 'message': 'unkonwn error'}
    
    return jsonify(res)
@app.route("/sindhudurg", methods=['GET'])
def sindhudurg():
    body = request.get_data()
    header = request.headers
    
    try:
        num1 = int(request.args['pC']) # Previous year crop yeild
        num2 = int(request.args['area']) # Area
        num3 = int(request.args['r1']) # last year rainfall
        num4 = int(request.args['r2']) # this year rainfall
        
        if((num1!=None) and (num2!=None) and (num3!=None) and (num4!=None)):
           res = predict_sindhudurg(num1, num2,num3,num4) # call the predict_sindhudurg function
        else:
           res = {'success': False,
                 'message': 'input proper data'}
           
    except:
           res = {'success': False,
                 'message': 'unkonwn error'}
    
    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True)          
