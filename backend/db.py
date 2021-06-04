from datetime import datetime
from pymongo import MongoClient
import hashlib

import config, filehandler

DB = None

def connect_db(host, database):
    global DB
    DB = MongoClient(host)[database]
    return DB

def insert_doc(uploader, title, description, tags, secret=None, filenam=None):

    doc = {
        "uploader": uploader, 
        "uploaded_at": datetime.utcnow(),
        "title": title,
        "description": description,
        "tags": tags, 
        "secret": None,
        "filenam": None
    }

    if(filenam is not None):
        file_attr = filehandler.saveFile(filenam)
        DB.get_collection(config.fileCol).insert_one(file_attr)
        doc["filenam"] = file_attr.get("uuid")
    
    #test data
    #doc["filenam"] = "test_file_name1"
    
    if(secret is not None):
        doc["secret"] = hashlib.sha256(secret.encode('utf-8')).hexdigest()

    return DB.get_collection(config.testCol).insert_one(doc)

def get_file(uuid):
    file_attr = DB.get_collection(config.fileCol).find_one({"uuid": uuid}, {"_id": 0})
    file = filehandler.getFile(file_attr.get("uuid"))
    mime = file_attr.get("mime")
    print(file)
    print(mime)
    return file, mime

def update_doc(name, age, date, new_name, new_age, new_date):
    query = {
        "name": name, 
        "age": age, 
        "date": date
    }
    new_doc = {
        "name": new_name, 
        "age": new_age, 
        "date": new_date
    }
    return DB.get_collection(config.testCol).update_one(query, {"$set": new_doc})

def get_doc(uploader, title, tags):
    query = dict()

    if uploader: 
        query["uploader"] = uploader
    
    if title: 
        query["title"] = title
    
    if tags: 
        tags_find_condition = dict()
        #find any data that correspond tag in tags
        tags_find_condition["$in"] = tags
        query["tags"] = tags_find_condition
    
    return list(DB.get_collection(config.testCol).find(query, {"_id": 0}))

def get_some_doc(begin, end):
    query = dict()
    return list(DB.get_collection(config.testCol).find(filter=query,projection={"_id":0}, skip=int(begin), limit=int(end)))

def delete_doc(secret, filenam):
    deleted_data = DB.get_collection(config.testCol).find_one({"filenam": filenam}, {"_id":0})
    target_secret = deleted_data.get("secret")
    if hashlib.sha256(secret.encode('utf-8')).hexdigest() == target_secret:
        query = {
            "filenam": filenam
        }

        return DB.get_collection(config.testCol).delete_one(query).acknowledged #刪除成功回傳true?

    return False  #讓server.py回傳錯誤?
    
    