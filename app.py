from crypt import methods
import json
import sys
import requests
from urllib import request
from flask import Flask, request, render_template, session, redirect, jsonify
from flask_session import Session
from helpers import login_required, apology

app = Flask('__name__')


# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


user =  {
        'id': 'id',
        'name': 'user1',
        'password': 'pass1'
    }

@app.route('/')
def index():

    return render_template('index.html')


@app.route('/home')
def home():

    return render_template('home.html')


# aingampanahy mitety ny abakabaka,
# volana sy kintana mandravaka



# LOGS
@app.route('/login', methods = ['POST', 'GET'])
def login():

    # clear session
    session.clear()

    # if method is not post
    if request.method == 'POST':
    
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        elif not user['name'] == request.form.get['username'] or not user['password'] == request.form.get['password']:
            return apology("password/username incorrect")

        session['user_id'] = user['id']

        return jsonify({'success': True, 'data': session['user_id']})

    else:
        return jsonify({'success': False,'error': 'method incorrect'})


@app.route('/logout')
def logout():

    # forget user
    session.clear()
    
    return redirect('/')



# ACCOUNTS
@app.route('/create_account', methods = ['POST'])
def create_account():
    ...
    # forget user
    # session.clear()

    # if request.form.get('username'):
    #     ...

    


@app.route('/update_account')
def update_account():
    ...


@app.route('/delete_account')
def delete_account():
    ...



# MESSAGES
@app.route('/send_message')
def send_message():
    ...


@app.route('/delete_message/<int:id>')
def delete_message(id):
    ...


# GROUP MESSAGES
@app.route('/create_group')
def create_group():
    ...

@app.route('/update_group')
def update_group():
    ...

@app.route('/delete_group')
def delete_group():
    ...

@app.route('/remove_from_group/<int:user_id>')
def remove_from_group(user_id):
    ...

