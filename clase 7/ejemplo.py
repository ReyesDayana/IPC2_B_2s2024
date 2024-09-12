from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola !'

@app.route('/ejemplo')
def ejemplo():
    return 'Esta es la ruta de ejemplo'

if __name__ == '__main__':
    app.run()