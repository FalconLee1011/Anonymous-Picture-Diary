import hashlib

from datetime import datetime
from pymongo import MongoClient, DESCENDING

import config, filehandler

DB = None


def connect_db(host, database):
    global DB
    DB = MongoClient(host)[database]
    return DB


def insert_doc(uploader, title, description, tags, secret=None, file=None):

    doc = {
        "uploader": uploader,
        "uploaded_at": datetime.utcnow(),
        "title": title,
        "description": description,
        "tags": tags,
        "secret": None,
        "filename": None,
    }

    if file is not None:
        file_attr = filehandler.saveFile(file)
        DB.get_collection(config.fileCol).insert_one(file_attr)
        doc["filename"] = file_attr.get("uuid")

    # test data
    # doc["filename"] = "test_file_name1"

    if secret is not None:
        doc["secret"] = hashlib.sha256(secret.encode("utf-8")).hexdigest()

    return DB.get_collection(config.postCol).insert_one(doc)


def get_file(uuid):
    file_attr = DB.get_collection(config.fileCol).find_one({"uuid": uuid}, {"_id": 0})
    file = filehandler.getFile(file_attr.get("uuid"))
    mime = file_attr.get("mime")
    print(file)
    print(mime)
    return file, mime


def update_doc(name, age, date, new_name, new_age, new_date):
    query = {"name": name, "age": age, "date": date}
    new_doc = {"name": new_name, "age": new_age, "date": new_date}
    return DB.get_collection(config.postCol).update_one(query, {"$set": new_doc})


def get_doc(uploader, title, tags):
    query = dict()

    if uploader:
        query["uploader"] = uploader

    if title:
        query["title"] = title

    if tags:
        tags_find_condition = dict()
        # find any data that correspond tag in tags
        tags_find_condition["$in"] = tags
        query["tags"] = tags_find_condition

    return list(DB.get_collection(config.postCol).find(query, {"_id": 0}))


def get_some_doc(begin, end):
    query = dict()
    return list(
        DB.get_collection(config.postCol)
        .find(filter=query, projection={"_id": 0}, skip=int(begin), limit=int(end))
        .sort("uploaded_at", DESCENDING)
    )


def delete_doc(secret, filename):
    deleted_data = DB.get_collection(config.postCol).find_one(
        {"filename": filename}, {"_id": 0}
    )
    target_secret = deleted_data.get("secret")
    if hashlib.sha256(secret.encode("utf-8")).hexdigest() == target_secret:
        query = {"filename": filename}

        return DB.get_collection(config.postCol).delete_one(query).acknowledged

    return False


def search_doc(keyword):
    query = {
        "$or": [
            {"uploader": {"$regex": keyword}},
            {"title": {"$regex": keyword}},
            {"description": {"$regex": keyword}},
            {"tags": {"$regex": keyword}},
        ]
    }
    res = list(
        DB.get_collection(config.postCol)
        .find(query, {"_id": 0})
        .sort("uploaded_at", DESCENDING)
    )

    print(query)
    print(res)

    return res
