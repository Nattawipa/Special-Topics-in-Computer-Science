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

    # [#2] YOUR CODE HERE - Preprocess
    value = D.preprocess(data)

    # [#3] YOUR CODE HERE - Predictions
    output = int(M.predict(value))

    data['Survived'] = output
    return json.dumps(data)

@app.route('/')
def index():
    '''Start page for testing.'''
    return 'Welcome to ITCS498 @ MUICT'
@app.route('/sample', methods=['GET'])
def sample():
    '''
    RESTful API used to test the prediction API by simulating one sample,
    package such sample in a JSON file, and send a HTTP POST to the prediction API.
    '''
    # [#1] YOUR CODE HERE - Sample data
    payload = {
                    'Age': 38.0,
                    'Cabin': 'C85',
                    'Embarked': 'C',
                    'Fare': 71.2833,
                    'Name': 'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
                    'Parch': 0,
                    'PassengerId': 2,
                    'Pclass': 1,
                    'Sex': 'female',
                    'SibSp': 1,
                    # 'Survived': 1,
                    'Ticket': 'PC 17599'
              }

    # Send a HTTP POST to the prediction API
    r = requests.post (
        'http://localhost:5000/predict', data = json.dumps(payload)
        )
    return r.json()

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = False)