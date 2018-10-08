from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup.html')

@app.route("/", methods=['POST'])
def signup():

    username =  request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    counter = 0
    password_error = ''
    user_error = ''
    email_error = ''
    confirm_error = ''

    for letters in username:
        if letters == ' ':
            user_error = 'Your username may not contain any spaces'
    for letters in password:
        if letters == ' ':
            password_error = 'Your password may not contain any spaces'
    for letters in email:
        if letters == ' ':
            email_error = 'Your email may not contain any spaces'
    for letters in email:
        if letters == "@" or letters == ".":
            counter += 1
    
    if counter != 2:
        email_error = 'Invalid email address'

    if len(username) < 3 or len(username) > 20:
        user_error = 'Your username must be between 3 and 20 characters long'
        username = ''
    if len(password) < 3 or len(password) > 20:
        password_error = 'Your password must be between 3 and 20 characters long'
        password = ''
    if len(email) < 3 or len(email) > 20:
        email_error = 'Your email must be between 3 and 20 characters long'
        email = ''
    if len(username) == 0:
        user_error = 'Please enter a username'
        username = ''
    if len(password) == 0:
        password_error = 'Please enter a password'
        password = ''
    if len(verify) == 0:
        confirm_error = 'Please enter and confirm a password'
        verify = ''
    if not password == verify:
        confirm_error = 'Password and confirmation do not match'
        password = ''
        verify = ''
    if not user_error and not password_error and not confirm_error and not email_error:
        return render_template('welcome-user.html', username=username)
    
    else:
        return render_template('signup.html', user_error=user_error, password_error=password_error,
        confirm_error=confirm_error, email_error=email_error)




app.run()