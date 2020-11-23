from flask import Flask, json, jsonify, request, Response
from flask_cors import CORS
from appointment import *
from register import *
from login import *
from forgot import *
from validateotp import *
from changepass import *
from confirmcart import *
from createcart import *
from getcart import *

app = Flask(__name__)
CORS(app)

# client=MongoClient(("mongodb://localhost:27017/"))
# mydb= client[]
# print("databae",client.list_database_names())

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
    userid = request.args.get('userid')
    message = Register(fname, lname, email, password,userid)
    return jsonify(message)


@app.route("/login")
def log():
    email = request.args.get('email')
    password = request.args.get('password')
    msg = Login(email, password)
    return jsonify(msg)


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

@app.route("/confirmcart")
def confirm():
    getitem = request.args.get('getitem')
    message = Cart(getitem)
    return jsonify(message)

@app.route("/createcart")
def create():
    userid = request.args.get('userid')
    message = CreateCart(userid)
    return jsonify(message)

@app.route("/getcart")
def get():
    userid = request.args.get('userid')
    message = getCart(userid)
    return message


if __name__ == " __main__ ":
    app.run(debug=True)
