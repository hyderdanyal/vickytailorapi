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
    # DELETE DATA
    # res = authentication.delete_many({})
    # print(res.deleted_count, "deleted")
    # print("shabahs", auth_data['email'])
    distinctemail = db['authentication'].distinct("email")
    print("alalala", distinctemail)
    # print("qqqq", type(distinctemail))
    if auth_data['email'] in distinctemail:
        # print(mail)
        return ("Email Exists")
    else:
        # print('ASD', mail)
        result = authentication.insert_one(auth_data)
        return ('Success')
    # print('One post: {0}'.format(result.inserted_id))
    display = authentication.find()
    for auth in display:
        print('Data in auth: ', auth)
    # delete all docs
    # print collections
    # print(db.list_collection_names())
