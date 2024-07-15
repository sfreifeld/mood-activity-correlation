from flask import Flask, request, redirect, jsonify
#from fitbit import fetch_activity_data

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the Fitbit OAuth Flow!'




if __name__ == '__main__':
       app.run(host='127.0.0.1', port=3000)