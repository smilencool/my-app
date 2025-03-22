from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return 'Welcome to python Flask'
if _name_='_main_':
    app.run(host='0.0.0.0',port=8080)
