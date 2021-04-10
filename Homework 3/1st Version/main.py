import data as D
import model as M

data1 = {
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

data2 = {
           #'target' = -1,
            'age' : 69,
            'sex' : 'M',
            'num1' : 120,
            'num2' : 229,
            'num3' : 129,
            'num4' : 2.6,
            'num5' : 3,
            'ord1' : 0,
            'ord2' : 0,
            'ord3' : 0,
            'ord4' : 1,
            'ord5' : 1,
            'ord6' : 2
        }

data = data1

# Preprocess
#print(data)
value = D.preprocess(data)
#print(value)

# Prediction
output = M.predict(value)

print(f'Data: {data}')
print(f'Target: {output}')
