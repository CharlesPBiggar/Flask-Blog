#Flask Routes
# Dependencies
import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, UpdateAccoutForm
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

# function to save picture and randomize picture names so that there are no collisions in the db
def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    #image resizing to save space in db
    output_size = (125,125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


#Account Route
@app.route('/account', methods=['POST', 'GET'])
@login_required
def account():
    form = UpdateAccoutForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email 
    image_file = url_for('static', filename=(f'profile_pics/{current_user.image_file}'))
    return render_template('account.html', title='Account', image_file=image_file, form=form)