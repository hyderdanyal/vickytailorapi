from pymongo import MongoClient

def CreateCart(userid):
    client = MongoClient()
    client = MongoClient('localhost', 27017)
    db = client.vickytailor

    cart=db.cart
    cart_data={
        'userid': userid
        
    }
    updatecart=cart.insert_one(cart_data)
    return("Cart Created")