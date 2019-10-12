from flask import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/historicalData')
def historical_data():
    return render_template('historicalData.html')

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