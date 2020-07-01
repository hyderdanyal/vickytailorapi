from pymongo import MongoClient

# passwo = "123"
# mail = "hyderdanyal@gmail.com"


def change(passwo, mail):
    print(passwo)
    client = MongoClient()
    client = MongoClient('localhost', 27017)
    db = client.vickytailor
    authentication = db.authentication

    # distinctemail = db['authentication'].distinct("email")
    for data in authentication.find():
        print(data)
        print("mail", mail)
        print("email", data['email'])
        print(data['password'])
        if (mail == data['email']):
            print("same")
            authentication.update_one(
                {"email": mail}, {"$set": {"password": passwo}})
            print("new password", data["password"])

            #     data['password'] == passwo
            #     print("changed", mail)
            #     return ("Password Change Successful")
            # else:
            #     print("didnt", mail)
            #     return ("Password Didnt change", data['email'])
        else:
            print("lalala")
