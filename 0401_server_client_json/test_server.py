from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'sever is alive'

@app.route('/predict')
def predict():
    return 'Predit...'

if __name__=='__main__':
    app.run()