from flask import Flask,render_template
app = Flask(__name__)



@app.route("/")
def hello():
    return "Hello world"

@app.route("/members")
def members():
    return "Members"

@app.route("/hello")
def hello_guys():
    return "Hello"

@app.route("/members/<name>")
def member_name(name):
    return render_template('index.html',name = name)


if __name__ == "__main__":
    app.run(debug=True)