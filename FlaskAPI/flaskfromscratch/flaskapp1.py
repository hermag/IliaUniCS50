from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    # Create a JSON object
    response_data = {
        'message': 'Hello, Flask!',
        'status': 'success'
    }

    # Convert the dictionary to a JSON response
    return jsonify(response_data)

@app.route('/cs50', methods=['GET'])
def cs50():
    # Create a JSON object
    response_data = {
        'message': 'Show this message in CS50!',
        'status': 'success'
    }

    # Convert the dictionary to a JSON response
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)