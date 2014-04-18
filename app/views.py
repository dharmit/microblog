from app import app
from flask import render_template, flash, redirect
from forms import LoginForm

@app.route('/')
@app.route('/index')
@app.route('/index.html')
@app.route('/home')
def index():
    #return "Hello, World"
    user = {"nickname": "Python"}
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
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", \
              remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
                            title = 'Sign In',
                            form = form,
                            providers = app.config['OPENID_PROVIDERS'])
