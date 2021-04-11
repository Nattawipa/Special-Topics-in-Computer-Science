from flask import Flask, request
import requests
import json
import data as D
import model as M

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    '''
    RESTful API that reads input data from a JSON data in HTTP POST.
    '''
    data = request.data.decode('utf-8')
    data = json.loads(data)
    # YOUR CODE HERE - Preprocess]
    value =[]
    for i in data:
        value.append(D.preprocess(i))

    # YOUR CODE HERE - Predictions
    output =[]
    for i in value:
        output.append(int(M.predict(i)))

    # YOUR CODE HERE - Return a JSON format
    count =0
    for i in data:
        i['target'] = output[count]
        count = count + 1
    return {"data":json.dumps(data)}

@app.route('/')
def index():
    '''Start page for testing.'''
    return '!! Nattawipa Homework 3 !!'

@app.route('/sample', methods=['GET'])
def sample():
    '''
    RESTful API used to test the prediction API by simulating one sample, 
    package such sample in a JSON file, and send a HTTP POST to the prediction API.
    '''
    # YOUR CODE HERE - Sample data
    payload = [
                #first data
                {
                    #'target' = -1,
                    'age' : 69,
                    'sex' : 'M',  
                    'num1' : 160,
                    'num2' : 286,
                    'num3' : 108,
                    'num4' : 1.5,
                    'num5' : 2,
                    'ord1' : 0,
                    'ord2' : 0,
                    'ord3' : 0,
                    'ord4' : 1,
                    'ord5' : 1,
                    'ord6' : 3
              },
              #second data
              {
                    #'target' = -1,
                    'age' : 69,
                    'sex' : 'M',
                    'num1' : 120,
                    'num2' : 229,
                    'num3' : 129,  #69,1,120,229,129,2.6,3,,,,1,1,2
                    'num4' : 2.6,
                    'num5' : 3,
                    'ord1' : 0,
                    'ord2' : 0,   
                    'ord3' : 0,
                    'ord4' : 1,
                    'ord5' : 1,
                    'ord6' : 3
              },
              #third data
              {
                    #'target' = -1,
                    'age' : 64,
                    'sex' : 'F',
                    'num1' : 140,
                    'num2' : 268,
                    'num3' : 160,  
                    'num4' : 3.6,
                    'num5' : 2,
                    'ord1' : 0,
                    'ord2' : 0,   
                    'ord3' : 0,
                    'ord4' : 0,
                    'ord5' : 0,
                    'ord6' : 2
              }]

    # if in case of NULL value
    for i in payload:
        for j in i:
            if j is None: 
                j = 0

    # Send a HTTP POST to the prediction API
    r = requests.post ( 'http://localhost:5000/predict', data = json.dumps(payload) )
    res = r.json()
    print("Nattawipa",res['data'])
    return res['data']

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = False)