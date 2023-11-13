from flask import Flask, render_template
import requests
import post

app = Flask(__name__)


@app.route('/')
def home():
    api_endpoint = 'https://api.npoint.io/5f448037c6c74b96f00b'
    api_response = requests.get(api_endpoint).json()
    return render_template("index.html", posts=api_response)


@app.route('/blog/<num>')
def get_post(num):
    api_endpoint = 'https://api.npoint.io/5f448037c6c74b96f00b'
    api_response = requests.get(api_endpoint).json()
    return render_template('post.html', post_id=int(num), posts=api_response)


if __name__ == "__main__":
    app.run(debug=True)
