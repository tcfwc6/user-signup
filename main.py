from flask import Flask, request, redirect, render_template
import cgi
import os 
import jinja2

app = Flask(__name__)
app.config["DEBUG"] = True 

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def validate():

    username = request.form["username"]
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if len(username) < 3 or len(username) > 20:
        username_error = "Invalid Username"
        username = ""
    else:
        if " " in str(username):
            username_error = "Space in username"
            username = ""
    
    if len(password) < 3 or len(password) > 20:
            password_error = "Invalid Password Length"
            password = ""
    else:
        if " " in str(password):
            password_error = "Space in password"
            password = ""

    if password != verify:
        verify_error = "Passwords do not match"
        verify = ""
    
    elif len(verify) < 3 or len(verify) > 20:
        verify_error = "Invalid Verify Length"
        verify = ""
    else:
        if " " in verify:
            verify_error = "Space in verify"
            verify = ""
        
    if email:
        if len(email) < 3 or len(email) > 20 or " " in email or email.count('@') > 1 or email.count('.') > 1:
           email_error = "Please enter a valid email address."
           email = ""

    if not username_error and not password_error and not verify_error and not email_error:
        username = str(username)
        return redirect("/welcome?username={0}".format(username))
    else:
        return render_template("index.html",
            username_error=username_error,
            password_error=password_error,
            verify_error=verify_error,
            email_error=email_error)  

@app.route("/welcome")
def welcome():
    username = request.args.get('username')
    return 'Welcome,{0}'.format(username)  

if __name__ == "__main__":
    app.run()