from flask import Flask
app = Flask(__name__)
@app.route('/flask')
def hello():
 return "Hello from flusk"
@app.route('/chintu')
def bello():
 return "Hello from chintu"
@app.route('/python')
def cello():
 return "Hello from python"
if __name__ == '_main_':
 app.run(host='0.0.0.0', port=5000)