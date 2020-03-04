# Charles Biggar - Flask Blog V1
# Dependencies
from flask import Flask, render_template, url_for
app = Flask(__name__)

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
@app.route("/")
@app.route("/home")
def hello():
    return render_template("home.html", posts=posts)

@app.route('/about')
def about():
    return render_template("about.html", title = "About")



#Debug Mode = Active
if __name__ == '__main__':
    app.run(debug=True)