from pymongo import MongoClient


def Login(email, password):
    client = MongoClient()
    client = MongoClient('localhost', 27017)
    db = client.vickytailor
    authentication = db.authentication
    auth_data = {
        'email': email,
        'password': password
    }
    display = authentication.find()
    for auth in display:
        # print(auth)
        if auth['email'] == auth_data['email']:
            if auth_data['password'] == auth['password']:
                print('USERID',auth['userid'])
                return ("Login Success",auth['userid'])
                
            else:
                return (" Incorrect Password")
        else:
            return(" No Such Email")
