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

    # YOUR CODE HERE - Preprocess
    value = D.preprocess(data)

    # YOUR CODE HERE - Predictions
    output = int(M.predict(value))

    # YOUR CODE HERE - Return a JSON format
    data['target'] = output
    return json.dumps(data)
  

@app.route('/')
def index():
    '''Start page for testing.'''
    return 'Welcome to Nattawipa Prediction !'

@app.route('/sample', methods=['GET'])
def sample():
    '''
    RESTful API used to test the prediction API by simulating one sample,
    package such sample in a JSON file, and send a HTTP POST to the prediction API.
    '''
    # YOUR CODE HERE - Sample data
    payload = {
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
              }
    # if in case of NULL value
    for i in payload:
        print(payload[i])
        if payload[i] is None: 
            payload[i] = 0 

    # Send a HTTP POST to the prediction API
    r = requests.post (
        'http://localhost:5000/predict', data = json.dumps(payload)
        )
    return r.json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)

