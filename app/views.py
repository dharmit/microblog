from app import app
from flask import render_template, flash, redirect
from forms import LoginForm

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
            user = user)
            #posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html',
                            title = 'Sign In',
                            form = form)
