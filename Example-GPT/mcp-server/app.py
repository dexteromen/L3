from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "UP"}), 200

@app.route('/status', methods=['GET'])
def status():
    return jsonify({
        "mcp": "running",
        "connections": 5,
        "tasks": ["task1", "task2"]
    }), 200

@app.route('/control', methods=['POST'])
def control():
    data = request.json
    action = data.get("action", "none")
    return jsonify({"message": f"Action '{action}' received and executed."}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
