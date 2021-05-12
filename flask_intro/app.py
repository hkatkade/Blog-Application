from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, Sourav!"

@app.route('/hi')
def hi():
    return "hello!"

@app.route('/user(username)')
def user():
    return "hello username: " #%escape(username)

if __name__ == "_main_":
    app.run(host='0.0.0.0',debug=True)