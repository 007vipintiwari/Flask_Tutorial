from flask import Flask,render_template
import datetime
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    current_year = datetime.datetime.now().year
    return render_template('index.html',year = current_year)

@app.route('/guess/<name>')
def guess_name(name):
    agify = "https://api.agify.io"
    params = {
        'name': name
    }
    agify_response = requests.get(agify,params= params)
    if agify_response.status_code == 200:
        age = agify_response.json()["age"]

    genderize_url = "https://api.genderize.io"
    param = {
        'name' : name
    }
    genderize_response = requests.get(genderize_url,params=param)
    if genderize_response.status_code == 200:
        gender = genderize_response.json()["gender"]

    return render_template('index.html',name=name,age=age,gender=gender)

@app.route('/blog')
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)

    if blog_response.status_code == 200:
        return render_template('blogs.html',blogs=blog_response.json())

if __name__ == "__main__":
    app.run(debug=True)