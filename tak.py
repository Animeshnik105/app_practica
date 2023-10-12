from flask import Flask
app = Flask(__name__)

@app.route('/')
def tak_tak_tak():
    return 'Tak tak tak'

