from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
     return "This is the first test using Flask"


app.run()