from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1})

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.json
        if not data or "data" not in data or not isinstance(data["data"], list):
            return jsonify({"is_success": False, "error": "Invalid input format"}), 400

        numbers = [item for item in data["data"] if item.isdigit()]
        alphabets = [item for item in data["data"] if item.isalpha()]
        highest_alphabet = max(alphabets, key=str.upper) if alphabets else []

        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": [highest_alphabet] if highest_alphabet else []
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
