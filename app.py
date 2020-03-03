# Charles Biggar - Flask Blog V1
# Dependencies
from flask import Flask


app = Flask(__name__)


#First Route
@app.route("/")
@app.route("/home")
def hello():
    return "<h1>Hello World!</h1>"

@app.route('/about')
def about():
    return "<h2>About Page</h2>"



#Debug Mode = Active
if __name__ == '__main__':
    app.run(debug=True)