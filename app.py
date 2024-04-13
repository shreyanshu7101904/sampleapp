from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.get("/")
def hello():
    return jsonify(name="hello")

if __name__ == '__main__':
    
    app.run(host="127.0.0.1", port=5000, debug=True)

