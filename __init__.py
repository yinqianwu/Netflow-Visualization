from flask import Flask, render_template, jsonify, flash, request, url_for, redirect,session
from content_management import Content
from wtforms import Form, BooleanField, TextField,PasswordField,validators
# from dbconnect import connection
# from passlib.hash import sha256_crypt
# from MySQLdb import escape_string as thwart
# import gc
import os
import numpy as np
import subprocess
import pprint
import json
import datetime
from restful import restapi

TOPIC_DICT = Content()

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("main.html")



@app.route('/dashboard/')
def dashboard():
	flash("still testing!!!")
	return render_template("dashboard.html", TOPIC_DICT = TOPIC_DICT)   


@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html")

# @app.errorhandler(405)
# def method_not_found(e):
# 	return render_template("405.html")


# @app.route('/login/', methods=['GET','POST'])
# def login_page():
# 	error = ''


# 	try:
# 		if request.method =="POST":
# 			attempted_username = request.form['username']	
# 			attempted_password = request.form['password']	

# 			# flash(attempted_username)
# 			# flash(attempted_password)

# 			if attempted_username =="admin" and attempted_password	=="password":
# 				return redirect(url_for('dashboard'))
# 			else:
# 				error="Invalid credentials. Try again!"

# 		return render_template("login.html", error = error)

# 	except Exception as e:
# 		# flash(e)
# 		return render_template("login.html", error = error)



# class RegistrationForm(Form):
# 	username = TextField('Username',[validators.Length(min=4,max=20)])
# 	email = TextField('Email Address',[validators.Length(min=4,max=20)])
# 	password = PasswordField('Password',[validators.Required(),
# 							validators.EqualTo('confirm',message="passwords must match.")])
# 	confirm = PasswordField('Repeat Password')
# 	accept_tos = BooleanField('I accept the Terms of Service')




# @app.route('/register/', methods=['GET','POST'])
# def register_page():
# 	try:
# 		# c,conn = connection()
# 		# return ("okey")
# 		form  = RegistrationForm(request.form)

# 		if request.method == "POST" and form.validate():
# 			username = form.username.data
# 			email = form.email.data
# 			password = sha256_crypt.encrypt((str(form.password.data)))
# 			c,conn = connection()

# 			x = c.execute("SELECT * FROM users WHERE usernme = (%s)",(thwart(username)))

# 			if int(x) > 0:
# 				flash("username is already taken")
# 				return render_template('register.html', form = form)

# 			else:
# 				c.execute("INSERT INTO users(username, password, email, tracking) VALUES (%s,%s,%s,%s)",
# 							(thwart(username),thwart(password),thwart(email)))
# 				conn.commit()
# 				flash("thanks for registering")
# 				c.close()
# 				conn.close()
# 				gc.collect()
# 				session['logged_in']=True
# 				session['username']= username
# 				return redirect(url_for('dashboard'))
# 		return render_template('register.html', form = form)


	# except Exception, e:
	# 	return render_template("404.html")


@app.route('/netflowapi/', methods=['GET'])
def returnAll():
	json_data = restapi()

	return json_data

 
if __name__ == "__main__":
    app.run(debug=True)

