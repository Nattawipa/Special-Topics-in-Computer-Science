import joblib

'''
You may write the code to load the model here, such that
the model is only loaded once at when we start the Flask server.

This can help save time re-loading the model for each request.

Here is an example from Workshop 9:

# Load model
model_file = 'model.joblib'
model = joblib.load(model_file)
'''
# YOUR CODE HERE

# Load model
model_file = 'model.joblib'
model = joblib.load(model_file)

def predict(value):
    '''Make predictions for the input `value`.'''
    pred = model.predict([value])
    
    return pred[0]
