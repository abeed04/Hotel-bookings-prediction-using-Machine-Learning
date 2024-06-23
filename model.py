import pickle
import numpy as np
import pandas as pd
import sklearn
df = pd.read_csv('Clean_hotel_data')

x = df.drop(['is_canceled','id'],axis=1)
y = df['is_canceled']

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=786)
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=201)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

pickle.dump(model,open("model.pkl","wb"))



