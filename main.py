from flask import *
import os
import predict
import numpy as np
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/historicalData')
def historical_data():
    options = list(map(lambda n: n.split('.')[0], os.listdir('data')))
    return render_template('historicalData.html', datasets=options)

pred_cache = {}

@app.route('/historicalData/<setname>')
def historical_data_display(setname):
    if setname not in pred_cache:
        pred_cache[setname] = predict.predict('data\\' + setname + '.csv')

    history, data = pred_cache[setname]
    data = data[['ds', 'yhat_lower', 'yhat_upper', 'yhat']]
    data['ds'] = data['ds'].apply(str)
    return render_template('predictionVis.html', history=np.array(history).tolist(), prediction=np.array(data).tolist(), title=setname)

@app.route('/liveData')
def live_data():
    return render_template('liveData.html')

@app.route('/plan')
def planner():
    return render_template('plan.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
  app.run()