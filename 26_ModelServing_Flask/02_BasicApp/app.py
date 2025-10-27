from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the basic Flask API!'

@app.route('/square', methods=['POST'])
def square_number():
    data = request.get_json() # Get JSON from client
    num = data['number']
    result = num * num
    return jsonify({'number': num, 'square': result})

if __name__ == '__main__':
    app.run(debug=True)