from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# load saved model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return "Welcome to the Iris Prediction API"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    prediction = model.predict(features)[0]
    return jsonify({'prediction':int(prediction)})

if __name__ == '__main__':
    app.run(debug=True)