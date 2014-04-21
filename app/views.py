from app import app, db, lm, oid
from flask import render_template, flash, redirect, session, url_for, \
        request, g
from forms import LoginForm
from flask.ext.login import login_user, logout_user, current_user, \
        login_required
from models import User, ROLE_USER, ROLE_ADMIN

@app.route('/')
@app.route('/index')
@login_required
def index():
    #return "Hello, World"
    user = g.user
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
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])
        #flash('Login requested for OpenID="' + form.openid.data + '", \
        #      remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
                            title = 'Sign In',
                            form = form,
                            providers = app.config['OPENID_PROVIDERS'])

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == '':
        flash("Invalid login. Please try again.")
        return redirect(url_for('login'))
    user = User.query.filter_by(email = resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == '':
            nickname = resp.email.split('@')[0]
        user = User(nickname = nickname, email = resp.email, role = ROLE_USER)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/usr/<nickname>')
@login_required
def user(nickanme):
    user = User.query.filter_by(nickanme = nickname).first()
    if user = None:
        flash('User' + nickname + 'not found')
        return redirect(url_for('index'))
    posts = [
            {'author': user, 'body': 'Test Post #1'},
            {'author': user, 'body': 'Test Post #2'}
            ]
    return render_template('user.html',
                          user = user
                          posts = posts
                          )
