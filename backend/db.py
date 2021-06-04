from pymongo import MongoClient

import config, filehandler

DB = None

def connect_db(host, database):
    global DB
    DB = MongoClient(host)[database]
    return DB

def insert_doc(name, age, date, file=None):

    doc = {
        "name": name, 
        "age": age, 
        "date": date, 
        "file": None
    }

    if(file is not None):
        file_attr = filehandler.saveFile(file)
        DB.get_collection(config.fileCol).insert_one(file_attr)
        doc["file"] = file_attr.get("uuid")

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

def get_doc(name, age, date):
    query = dict()

    if name: 
        query["name"] = name
    
    if age: 
        query["age"] = age
    
    if date: 
        query["date"] = date
    
    return list(DB.get_collection(config.testCol).find(query, {"_id": 0}))

def get_some_doc(begin, end):
    query = dict()
    return list(DB.get_collection(config.testCol).find(filter=query,projection={"_id":0}, skip=int(begin), limit=int(end)))

def delete_doc(name, age, date):
    query = {
        "name": name, 
        "age": age, 
        "date": date
    }
    return DB.get_collection(config.testCol).delete_one(query)
