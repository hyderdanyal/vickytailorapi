from flask import Flask, json, jsonify, request, Response
from flask_cors import CORS
from appointment import *
from register import *
from login import *
from forgot import *
from validateotp import *
from changepass import *

app = Flask(__name__)
CORS(app)


@app.route("/changepass")
def passwo():
    password = request.args.get('password')
    email = request.args.get('email')
    # return ("TESTEMAILPASS", email, password)
    res = change(password, email)
    return jsonify(res)


@app.route("/forgot")
def forget():
    email = request.args.get('email')
    mssg = Forgot(email)
    return jsonify(mssg)


@app.route("/register")
def reg():
    fname = request.args.get('fname')
    lname = request.args.get('lname')
    email = request.args.get('email')
    password = request.args.get('password')
    message = Register(fname, lname, email, password)
    return jsonify(message)


@app.route("/login")
def log():
    email = request.args.get('email')
    password = request.args.get('password')
    msg = Login(email, password)
    return(jsonify(msg))


@app.route("/submitpass")
def new():
    passw = request.args.get('changepass')
    mail = request.args.get('mail')
    res = change(passw, mail)
    return jsonify(res)


@app.route("/appointment")
def email():
    fname = request.args.get('fname')
    lname = request.args.get('lname')
    email = request.args.get('email')
    phone = request.args.get('phone')
    service = request.args.get('service')
    address = request.args.get('address')
    city = request.args.get('city')
    message = request.args.get('message')
    feedback(fname, lname, email, phone, service, address, city, message)
    return jsonify("Mail Sent")


@app.route("/validateotp")
def otp():
    checkotp = request.args.get('otp')
    email = request.args.get('email')
    res = validateotp(checkotp, email)
    return jsonify(res)


if __name__ == " __main__ ":
    app.run(debug=True)
