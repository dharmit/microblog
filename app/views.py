from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
@app.route('/index.html')
@app.route('/home')
def index():
    #return "Hello, World"
    user = {"nickname": "Dharmit"}
    posts = [
            {
                'author': {'nickname': 'Komal'},
                'body': 'Beautiful day in Pune'
            },
            {
                'author': {'nickname': 'Dharmit'},
                'body': 'Ahmedabad is anytime better.'
            }
            ]
    return render_template("index.html",
            title = "Home",
            user = user,
            posts = posts)
