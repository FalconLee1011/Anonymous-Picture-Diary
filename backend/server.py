from time import sleep

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

import db, config

app = Flask(__name__)
app.debug = True
CORS(app)

@app.route("/create-doc-with-attachment", methods=["POST"])
def create_doc_with_attachment():
    form = request.form
    uploader = form.get("uploader", "anonymous")
    if(len(uploader) == 0):
        uploader = "Anonymous | 匿名"
    secret = form.get("secret")
    #taken_at
    title = form.get("title", "no_title")
    description = form.get("description", "none")
    tags = form.get("tags", []).replace(" ", "").split(",")
    file = request.files.get("file")
    print(tags)
    
    #照片為必須的?因為刪除貼文是用照片的uuid去辨識
    if file is None:
        return "photo is required.", 422

    
    res = db.insert_doc(uploader, title, description, tags, secret, file)
    return "ok", 200

@app.route("/get-attachment", methods=["GET"])
def get_attachment():
    args = request.args
    uuid = args.get("uuid")
    if(uuid is None):
        return "File not specified", 422
    file, mime = db.get_file(uuid) 
    return send_file(file, mimetype=mime), 200

#not use
@app.route("/create-doc", methods=["POST"])
def create_doc():
    body = request.get_json()

    name = body.get("name", "unknown")
    age = body.get("age", "-")
    date = body.get("date")

    # Just for the effect.
    sleep(0.75)

    if date is None:
        return "Date is required.", 422
    
    res = db.insert_doc(name, age, date)
    return "ok", 200

#not use
@app.route("/update-doc", methods=["PUT"])
def update_doc():
    body = request.get_json()
    name = body.get("name")
    age = body.get("age")
    date = body.get("date")

    new_name = body.get("new_name")
    new_age = body.get("new_age")
    new_date = body.get("new_date")

    res = db.update_doc(name, age, date, new_name, new_age, new_date)
    return "Updated!", 200

@app.route("/get-doc", methods=["GET"])
def get_doc():
    args = request.args
    uploader = args.get("uploader")
    title = args.get("title")
    tags = args.get("tags")
    res = db.get_doc(uploader, title, tags)
    
    return jsonify(res), 200

@app.route("/search", methods=["GET"])
def search_doc():
    args = request.args
    keyword = args.get("keyword", "")
    res = db.search_doc(keyword)
    
    return jsonify(res), 200

@app.route("/get-some-doc", methods=["GET"])
def get_some_doc():
    args = request.args
    #begin: from which data
    #end: to which data
    begin = args.get("begin")
    end = args.get("end")
    res = db.get_some_doc(begin, end)
        
    return jsonify(res), 200


@app.route("/delete-doc", methods=["DELETE"])
def delete_doc():
    filename = request.args.get("filename")
    secret = request.headers.get("secret")
    print(filename)
    print(secret)
    res = db.delete_doc(secret, filename)

    if res:
        return "Deleted", 200
    
    return "No Authorization", 403

def printAvailableAPIs():
    basic_methods = ["GET", "POST", "PUT", "DELETE"]
    print("")
    print("  {:^40} | {:^15}".format("URL", "METHODS"))
    # Flask app's property "url_map" has a function iter_rules() to loop through all available APIs.
    for p in app.url_map.iter_rules():
        print("  {:<40} | {:<15}".format(str(p), ", ".join(set(p.methods).intersection(basic_methods))))
    print("")

def main():
    db.connect_db(config.host, config.db)
    printAvailableAPIs()
    app.run(host="0.0.0.0", port=9000, debug=True)


if __name__ == "__main__":
    main()