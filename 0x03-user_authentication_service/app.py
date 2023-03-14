from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello Flasky</h1>'

@app.route('/<name>')
def name(name):
    return f'<h1>{name}, Welcome to Flasky!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
