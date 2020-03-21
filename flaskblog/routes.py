#Flask Routes
# Dependencies
from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

# Dummy Post Data
posts = [
    {
        'author': 'Charles Biggar',
        'title': 'Blog Post 1',
        'content': 'Charles is working on his webpage',
        'date_posted': 'March 3, 2020'
    },
    {
        'author': 'Amanda Kramer',
        'title': 'Blog Post 2',
        'content': 'Amanda is currently working on SAS Homework!',
        'date_posted': 'March 3, 2020'
    }
]


#Home Route
@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html", title = "Home Page", posts=posts)

#About Page Route
@app.route('/about')
def about():
    return render_template("about.html", title = "About")

#Registration Page Route
@app.route('/register', methods=['POST','GET'])
def register():
    form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template("registration.html", title = "Registration Page", form=form)

#Login Route
@app.route('/login', methods=['POST','GET'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccesful. Please check email and password', 'danger')
    return render_template("login.html", title = "Login Page", form=form)

#Logout Route
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


#Account Route
@app.route('/account')
@login_required
def account():
    image_file = url_for('static', filename=(f'profile_pics/{current_user.image_file}'))
    return render_template('account.html', title='Account', image_file=image_file)