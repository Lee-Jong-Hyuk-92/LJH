from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load("lgbm_model.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        print("Received data:", data)
        df = pd.DataFrame(data)
        prediction = model.predict(df)
        return jsonify({'prediction': prediction.tolist()})
    
    except Exception as e:
        print("[ERROR]", e)
        return jsonify({'error': str(e)})


@app.route('/hello', methods=['GET'])
def hello():
    return 'Server is alive!'

if __name__ == '__main__':
    app.run('127.0.0.1', port=9999, debug=True)