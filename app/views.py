from flask import render_template, redirect
from flask import request
from flask_login import login_user, logout_user, login_required
from models import User
from app import app
from . import mysql
#sample user
user = User('admin','password')


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    #verify user
    cur = mysql.connection.cursor()
    cur.execute("Select * from login where username='"+username+"' and password='"+password+"'")
    data = cur.fetchone()
    if data:
        login_user(user)
        return redirect("/"+username)
    else:
        return abort(401)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route("/<username>")
@login_required
def home(username):
    return "Username: "+username