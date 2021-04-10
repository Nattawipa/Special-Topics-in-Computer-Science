from flask import Flask             # import Flask
app = Flask(__name__)               # create Flask object

@app.route('/')
def hello_world():
    return 'Mahidol University'

@app.route('/itcs498', methods = ['GET','POST'])
def function2():
    return 'ITCS498'

if __name__ == '__main__':
    app.run(debug = True)

