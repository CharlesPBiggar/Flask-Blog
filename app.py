# Charles Biggar - Flask Blog V1
# Dependencies
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'e94f492957e9be802f10ca325ee12cb3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
from models import User, Post

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
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("registration.html", title = "Registration Page", form=form)

#Login Route
@app.route('/login', methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Dummy login information - will be corrected when DB is built
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You are now logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccesful. Please check email and password', 'danger')
    return render_template("login.html", title = "Login Page", form=form)


#Debug Mode = Active
if __name__ == '__main__':
    app.run(debug=True)