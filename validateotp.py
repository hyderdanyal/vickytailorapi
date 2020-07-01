from pymongo import MongoClient


def validateotp(otp, email):
    client = MongoClient()
    client = MongoClient('localhost', 27017)
    db = client.vickytailor
    authentication = db.authentication

    distinctemail = db['authentication'].distinct("email")
    for data in authentication.find():
        if (email == data['email']):
            if (otp == data['otp']):
                return (True)
            else:
                return (False)
