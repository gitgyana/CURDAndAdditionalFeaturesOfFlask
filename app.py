from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return {"message": "You are running the default flask application"}