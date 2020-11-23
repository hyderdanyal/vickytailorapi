from pymongo import MongoClient

client = MongoClient()
dbnames = client.list_database_names()
print("ccc")
for db in dbnames:
    print("db",db)

client = MongoClient('localhost', 27017)
db = client.vickytailor
auth=db["authentication"]
data = {
    'title': 'Python and MongoDB',
    'content': 'PyMongo is fun, you guys',
    'author': 'Scott'
}
result = auth.insert_one(data)
print("posts" in db.list_collection_names())
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
