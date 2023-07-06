from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/sample/', methods=['GET'])
def welcome():
    response = jsonify([{'name':'Danyaal', 'address':'202 R block'}, 
                    {'name': 'Maaz', 'address':'342 J block'},
                    {'name': 'Umair', 'address':'423 C block'}])
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)