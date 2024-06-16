from flask import Flask
"""
A module's __name__ is set equal to __main__ when read from standard input,
a script or from an interactive prompt.
"""
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World"

if __name__ == "__main__":
    app.run()