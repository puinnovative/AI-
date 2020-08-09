from flask import Flask
from flask import redirect
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Hello World!</h1>' + '<p>Your browser is %s</p>' % user_agent


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


@app.route('/toGoogle')
def search():
    return redirect('http://www.google.co.uk')






if __name__ == '__main__':
    app.run(debug=True)