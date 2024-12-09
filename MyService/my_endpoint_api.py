from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/my_endpoint', methods=['GET', 'POST'])
def my_endpoint():
    if request.method == 'GET':
        return jsonify({"message": "GET request received at my_endpoint"})
    elif request.method == 'POST':
        data = request.json
        return jsonify({"message": "POST request received", "data": data})

if __name__ == "__main__":
    app.run(debug=True)