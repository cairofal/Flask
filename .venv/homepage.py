from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
     return render_template("homepage.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

@app.route("/users/<user_name>")
def users(user_name):
   return render_template("users.html", user_name=user_name)

if __name__ == "__main__":
 app.run(debug=True)

 #Deploy in Heroku 
