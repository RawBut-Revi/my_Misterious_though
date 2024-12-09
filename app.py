from flask import Flask, request, render_template
from models.statistical_model import StatisticalModel
from models.rl_model import train_rl_model
import pandas as pd
import numpy as np
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    model_type = request.form['model_type']
    if model_type == 'statistical':
        data = pd.read_csv('data/roulette_data.csv')
        model = StatisticalModel(data['number'])
        prediction = model.predict()
    elif model_type == 'reinforcement':
        Q = train_rl_model()
        prediction = np.argmax(Q[:, 0])  # Simple prediction using Q-table
    else:
        prediction = "Invalid model type selected."
    
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
