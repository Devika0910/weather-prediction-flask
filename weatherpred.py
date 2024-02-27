import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
dt=pd.read_csv("daily_weather (1).csv")
print(dt.head(5))


data=dt.fillna(dt.mean())
y=data['high_humidity_3pm'].copy()
x=data[['air_pressure_9am','air_temp_9am','avg_wind_direction_9am']].copy()
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=778)
clf=LinearRegression()
clf.fit(x_train,y_train)

from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def abc():
    return render_template('form.html')

@app.route('/output',methods=['GET','POST'])
def jgug():
    air_temp_9am=request.form['air_temp_9am']
    air_pressure_9am=request.form['air_pressure_9am']
    avg_wind_direction_9am=request.form['avg_wind_direction_9am']
    arr= np.array([air_pressure_9am,air_temp_9am,avg_wind_direction_9am])
    arr=arr.astype(np.float64)
    pred=clf.predict([arr])

    return render_template('output.html',pred=pred)

if __name__== '__main__':
    app.run(debug=True)






