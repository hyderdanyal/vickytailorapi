from pymongo import MongoClient
import json

# getitem="ddddd"

def Cart(getitem):
    client = MongoClient()
    client = MongoClient('localhost', 27017)
    db = client.vickytailor

    cart=db.cart
    print('GETITEM', getitem)
    getitem=json.dumps(getitem)
    cart_data={
        'item':getitem
        }
    print("data",cart_data)
    updatecart=cart.insert_one(cart_data)
    print("updatecart",updatecart)
    print("updateddata",cart_data)
    return("Cart Updated")
# Cart(getitem)
