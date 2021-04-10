from flask import Flask             # import Flask
app = Flask(__name__)               # create Flask object

@app.route('/')
def hello_world():
    return '6188089 Nattawipa Saetae'

@app.route('/6188089', methods = ['GET','POST'])
def function2():
    return 'Nattawipa Homework 3'

if __name__ == '__main__':
    app.run(debug = True)

