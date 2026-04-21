from flask import Flask, jsonify
import requests 

app = Flask(__name__)

API_URL = 'https://jsonplaceholder.typicode.com/users'

@app.route('/users', methods=['GET'])
def get_users():
    response = requests.get(API_URL)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
