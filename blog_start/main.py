from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    if blog_response.status_code == 200:
        return render_template('index.html',blogs=blog_response.json())
        # return render_template("index.html")

@app.route("/post/<int:id>")
def get_post(id):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    if blog_response.status_code == 200:
        result = blog_response.json()
        for blog in result:
            if blog["id"] == id:
                return render_template('post.html',blog=blog)
if __name__ == "__main__":
    app.run(debug=True)
