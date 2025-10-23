# Flask - micro web framework in Python - lightweight, simple, 
# small- medium web apps

from flask import Flask

app = Flask(__name__)

# define a simple route
@app.route('/aboutus')
def home():
    return 'Hello, Flask is running successfully'

if __name__ == '__main__':
    app.run(debug=True)