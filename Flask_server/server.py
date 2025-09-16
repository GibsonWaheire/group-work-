from flask import Flask, jsonify
from flask_cors import CORS  # Uncomment this line to enable CORS

app = Flask(__name__)
CORS(app)  # This line enables CORS for all routes

@app.route('/members')
def members():
    return jsonify({"members": ["members1", "members2", "members3"]})


if __name__ == '__main__':  
    app.run(debug=True) 

