from pymongo import MongoClient


def connect_db(host, database):
    db = MongoClient(host)
    return db[database]


def insert_doc(db, col, name, age, date):
    doc = {
        "name": name, 
        "age": age, 
        "date": date
    }
    return db.get_collection(col).insert_one(doc)

def update_doc(db, col, name, age, date, new_name, new_age, new_date):
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
    return db.get_collection(col).update_one(query, {"$set": new_doc})

def get_doc(db, col, name, age, date):
    query = dict()

    if name: 
        query["name"] = name
    
    if age: 
        query["age"] = age
    
    if date: 
        query["date"] = date

    return list(db.get_collection(col).find(query, {"_id": 0}))

def delete_doc(db, col, name, age, date):
    query = {
        "name": name, 
        "age": age, 
        "date": date
    }
    return db.get_collection(col).delete_one(query)
