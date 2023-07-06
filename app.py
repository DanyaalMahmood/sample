from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/sample/', methods=['GET'])
def sample():
    response = jsonify([{'name':'Danyaal', 'address':'202 R block'}, 
                    {'name': 'Maaz', 'address':'342 J block'},
                    {'name': 'Umair', 'address':'423 C block'}])
    return response


@app.route('/flow/', methods=['GET'])
def flow():
    data = {
            'initialNodes': [
                { 'id': '1', 'position': { 'x': 0, 'y': 0 }, 'data': { 'label': 'Design' } },
                { 'id': '2', 'position': { 'x': 0, 'y': 100 }, 'data': { 'label': 'Development' } },
                { 'id': '3', 'position': { 'x': 0, 'y': 200 }, 'data': { 'label': 'Testing' } },
                { 'id': '4', 'position': { 'x': 0, 'y': 300 }, 'data': { 'label': 'Deployment' } },
            ],
            'initialEdges': [ 
                { 'id': 'e1-2', 'source': '1', 'target': '2', 'style': {'strokeWidth': 2,'stroke': '#FF0072'}}, 
                { 'id': 'e2-3', 'source': '2', 'target': '3', 'style': {'strokeWidth': 2,'stroke': '#FF0072'} },
                { 'id': 'e3-4', 'source': '3', 'target': '4', 'style': {'strokeWidth': 2,'stroke': '#FF0072'} }
            ]
    }
    response = jsonify(data)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)