from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, It is me'

if __name__ == '__main__':
    app.run()