import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings('ignore')

data = pd.read_csv('heart.csv')
data.head()


dict = {}
for i in list(data.columns):
    dict[i] = data[i].value_counts().shape[0]

pd.DataFrame(dict,index=["unique count"]).transpose()


# Scaling
from sklearn.preprocessing import RobustScaler

# Train Test Split
from sklearn.model_selection import train_test_split


from sklearn.svm import SVC


# Metrics
from sklearn.metrics import accuracy_score, classification_report, roc_curve

# Cross Validation
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV

cat_cols = ['sex','exng','caa','cp','fbs','restecg','slp','thall']
con_cols = ["age","trtbps","chol","thalachh","oldpeak"]


# creating a copy of df
df1 = data

# encoding the categorical columns

# defining the features and target
X = df1.drop(['output'],axis=1)
y = df1[['output']]

# instantiating the scaler
scaler = RobustScaler()

# scaling the continuous featuree
X = scaler.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# instantiating the object and fitting --dt -random forest -
clf = SVC(kernel='linear', C=1, random_state=42).fit(X_train,y_train)
# predicting the values
y_pred = clf.predict(X_test)
# printing the test accuracy
print("The test accuracy score of SVM is ", accuracy_score(y_test, y_pred))

def predict_risk(age, sex, cp, trtbps, chol, fbs, restecg,
                 thalachh, exng, oldpeak, slp, caa, thall):
    input_data = [age, sex, cp, trtbps, chol, fbs, restecg,
                 thalachh, exng, oldpeak, slp, caa, thall]

    input_array = np.asarray(input_data).reshape(1, -1)

    prediction = clf.predict(input_array)

    prediction = clf.predict(input_array)[0]
    if prediction== 1:
      return 1
    else:
      return 0

def creating_model():
    needed_columns = ['age', 'sex', 'cp', 'trtbps', 'chol', 'fbs', 'restecg',
                      'thalachh', 'exng', 'oldpeak', 'slp', 'caa', 'thall']

    X = data[needed_columns]
    y = df1['output']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=48)

    model = SVC()
    model.fit(X_train, y_train)

    return model


model = creating_model()


import joblib
joblib.dump(model, 'model.pkl')