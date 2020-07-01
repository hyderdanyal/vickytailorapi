from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.vickytailor
# db = client['vickytailor']
# posts = db.posts
# post_data = {
#     'title': 'Python and MongoDB',
#     'content': 'PyMongo is fun, you guys',
#     'author': 'Scott'
# }
# result = posts.insert_one(post_data)
# print('One post: {0}'.format(result.inserted_id))
dataposts = db.authentication.find()
for post in dataposts:
    print('Data in DB: ', post)
