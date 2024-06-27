from flask import Flask
app = Flask(_name_)
@app.route('/flask')
def hello():
 return "Hello from flusk"
@app.route('/chintu')
def bello():
 return "Hello from chintu"
if _name_ == '_main_':
 app.run(host='0.0.0.0', port=5000)