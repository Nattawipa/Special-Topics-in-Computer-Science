import joblib

# Load model
model_file = 'model.joblib'
model = joblib.load(model_file)

def predict(value):
    # YOUR CODE HERE
    pred = model.predict([value])
    return pred[0]