from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
def greet():
    return 'Hello'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f')
@app.route('/f/<celsius>')
def convert_celsius_to_fahrenheit(celsius=" "):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = float(celsius) * 9.0 / 5 + 32
    return f"{fahrenheit:.2f}"


if __name__ == '__main__':
    app.run()
