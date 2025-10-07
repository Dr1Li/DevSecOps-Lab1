from flask import Flask, request, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route('/add', methods=['POST'])
def add():
    """Add two numbers"""
    try:
        data = request.get_json()
        if not data or 'a' not in data or 'b' not in data:
            return jsonify({'error': 'Missing parameters a and b'}), 400

        result = data['a'] + data['b']
        return jsonify({'operation': 'add', 'result': result, 'inputs': data})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/subtract', methods=['POST'])
def subtract():
    """Subtract two numbers"""
    try:
        data = request.get_json()
        if not data or 'a' not in data or 'b' not in data:
            return jsonify({'error': 'Missing parameters a and b'}), 400

        result = data['a'] - data['b']
        return jsonify({'operation': 'subtract', 'result': result, 'inputs': data})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/multiply', methods=['POST'])
def multiply():
    """Multiply two numbers"""
    try:
        data = request.get_json()
        if not data or 'a' not in data or 'b' not in data:
            return jsonify({'error': 'Missing parameters a and b'}), 400

        result = data['a'] * data['b']
        return jsonify({'operation': 'multiply', 'result': result, 'inputs': data})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/divide', methods=['POST'])
def divide():
    """Divide two numbers"""
    try:
        data = request.get_json()
        if not data or 'a' not in data or 'b' not in data:
            return jsonify({'error': 'Missing parameters a and b'}), 400

        if data['b'] == 0:
            return jsonify({'error': 'Division by zero not allowed'}), 400

        result = data['a'] / data['b']
        return jsonify({'operation': 'divide', 'result': result, 'inputs': data})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'message': 'Arithmetic API is running'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
