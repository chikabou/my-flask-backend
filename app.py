from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask server is running!"

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    return jsonify({"response": f"Hello, {data['username']}!"})

if __name__ == "__main__":
    app.run()
