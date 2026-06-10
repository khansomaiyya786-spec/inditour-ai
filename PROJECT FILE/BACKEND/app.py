from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "IndiTour AI Backend Running!"})

@app.route('/api/destinations')
def destinations():
    return jsonify({"data": "List of destinations"})

@app.route('/api/hotels')
def hotels():
    return jsonify({"data": "List of hotels"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)