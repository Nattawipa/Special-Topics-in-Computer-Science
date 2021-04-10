import numpy as np
from sklearn.preprocessing import OneHotEncoder

# Two values
sex_enc = OneHotEncoder(
    categories=[np.array(['M','F'])], drop='first')
sex_enc.fit(np.array(['M','F']).reshape(-1,1))

def preprocess(data):
    '''Convert from a dict to a vector.'''
    # One-hot encoding - sex
    sex_v = np.array([data['sex']]).reshape(-1,1)
    sex_v = sex_enc.transform(sex_v).toarray()
    value = [
                data['age'],
                sex_v[0][0], # Sex code
                data['num1'], data['num2'], 
                data['num3'], data['num4'], 
                data['num5'],  
                data['ord1'], data['ord2'], 
                data['ord3'], data['ord4'], 
                data['ord5'], data['ord6']
            ]
    return np.array(value)