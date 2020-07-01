from pymongo import MongoClient


def Register(fname, lname, email, password):
    # print('first' + fname)
    client = MongoClient()
    client = MongoClient('localhost', 27017)
    db = client.vickytailor

    # print documents
    # db = client['vickytailor']
    authentication = db.authentication
    # cursor = authentication.find({})
    # for document in cursor:
    #     print("abracadabra", document)
    auth_data = {
        'fname': fname,
        'lname': lname,
        'email': email,
        'password': password
    }
    result = authentication.insert_one(auth_data)
    # print('One post: {0}'.format(result.inserted_id))
    display = authentication.find()
    for auth in display:
        print('Data in auth: ', auth)
    # delete all docs
    # res = posts.delete_many({})
    # print(res.deleted_count, "deleted")
    # print collections
    # print(db.list_collection_names())
    # print(db['db'].distinct("_id"))
