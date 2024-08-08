from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Replace this with your prediction logic
    result = {'prediction': 'example'}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
