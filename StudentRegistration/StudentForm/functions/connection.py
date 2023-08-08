import pymongo
from pymongo.server_api import ServerApi
from StudentForm.functions.credentials import Credentials
# from credentials import Credentials
credentials = Credentials()
username = credentials.username
password = credentials.password
collection_name = credentials.collection
database = credentials.database
cluster = credentials.cluster

client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@{cluster}.jfxpkv7.mongodb.net/?retryWrites=true&w=majority", server_api=ServerApi('1'))
db=client[database]
collection=db[collection_name]

def upload_otp_name_uid(data):
    result = collection.insert_one(data)
    return {
        'success':True,
        'messsage': 'Parents Guide Data Uploaded Successfully to the Database',
        'inserted_id': str(result.inserted_id)
        }

def check_user(uid):
    query = {'uid': uid}
    document = collection.find_one(query)
    if document:
        if document['verified'] == True:
            return {"status":"exists"}
        else:
            return {"status":"exists-not-verified"}
    else:
        return {"status":"not-exists"}

def get_all_data(uid):
    query = {'uid': uid}
    document = collection.find_one(query)
    return document  

def verify_user(uid):
    query = {'uid': uid}
    update_query = {"$set": {"verified": True}}
    result = collection.update_one(query, update_query)
    if result.modified_count > 0:
        return True
    else:
        return False

def update_otp(uid, otp):
    query = {'uid': uid}
    update_query = {"$set": {"otp": otp}}
    result = collection.update_one(query, update_query)
    if result.modified_count > 0:
        return True
    else:
        return False

def update_details(data):
    uid = data['uid']
    query = {'uid': uid}
    update_query = {"$set": {
        "section":data["section"],
        "contact":data["contact"],
        "email":data["email"],
        "introduction":data["introduction"],
        "whyWorkWithUs":data["whyWorkWithUs"],
        "resume":data["resume"]   
        }}
    result = collection.update_one(query, update_query)
    if result.modified_count > 0:
        return True
    else:
        return False

if __name__ == "__main__":
    # upload_otp_name_uid({
    # "name": "ritik",
    # "uid": "21bcs9973",
    # "otp": 1231243
    # })
    print(check_user('21bcs9733'))