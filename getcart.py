from pymongo import MongoClient

def getCart(userid):
    client = MongoClient()
    client = MongoClient('localhost', 27017)
    db = client.vickytailor

    cart=db.cart
    cart_userid={
        'userid':userid
    }
    search=cart.find()
    for s in search:
        if s['userid'] == cart_userid['userid']:
            print("items",s['item'])
            return("search success")
        
        else:
            print("No sych user id")
            return("search not found")
        