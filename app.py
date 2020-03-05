# Charles Biggar - Flask Blog V1
# Dependencies
from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e94f492957e9be802f10ca325ee12cb3'

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


#First Route
@app.route('/')
@app.route('/home')
def hello():
    return render_template("home.html", title = "Home Page", posts=posts)

@app.route('/about')
def about():
    return render_template("about.html", title = "About")

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template("register.html", title = "Registration Page", form=form)

@app.route('/login')
def register():
    form = LoginForm()
    return render_template("login.html", title = "Login Page", form=form)


#Debug Mode = Active
if __name__ == '__main__':
    app.run(debug=True)