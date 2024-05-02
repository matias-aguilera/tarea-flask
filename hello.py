from flask import Flask,render_template

app = Flask(__name__)

posts=["post1","post2"] 

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"