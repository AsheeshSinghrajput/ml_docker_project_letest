from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello, Baby! Your API is running inside Docker "})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
