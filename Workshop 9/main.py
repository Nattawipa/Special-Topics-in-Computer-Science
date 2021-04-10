import data as D
import model as M

data1 = {
    'Age': 22.0,
    'Cabin': 'UNK',
    'Embarked': 'S',
    'Fare': 7.25,
    'Name': 'Braund, Mr. Owen Harris',
    'Parch': 0,
    'PassengerId': 1,
    'Pclass': 3,
    'Sex': 'male',
    'SibSp': 1,
    # 'Survived': 0,
    'Ticket': 'A/5 21171'}

data2 = {
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
    'Ticket': 'PC 17599'}

data = data1

# Preprocess
print(data)
value = D.preprocess(data)
print(value)

# Prediction
output = M.predict(value)

print(f'Data: {data}')
print(f'Survived: {output}')
