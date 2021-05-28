from time import sleep

from flask import Flask, request, jsonify
from flask_cors import CORS

import db, config

app = Flask(__name__)
app.debug = True
CORS(app)

DB = None

@app.route("/create-doc", methods=["POST"])
def create_doc():
    body = request.get_json()
    name = body.get("name", "unknown")
    age = body.get("age", "-")
    date = body.get("date")

    # Just for the effect.
    sleep(0.75)

    if date is None:
        return "Date is required."
    
    res = db.insert_doc(DB, config.testCol, name, age, date)
    return "ok", 200

@app.route("/update-doc", methods=["PUT"])
def update_doc():
    body = request.get_json()
    name = body.get("name")
    age = body.get("age")
    date = body.get("date")

    new_name = body.get("new_name")
    new_age = body.get("new_age")
    new_date = body.get("new_date")

    res = db.update_doc(DB, config.testCol, name, age, date, new_name, new_age, new_date)
    return "Updated!", 200

@app.route("/get-doc", methods=["GET"])
def get_doc():
    args = request.args
    name = args.get("name")
    age = int(args.get("age"))
    date = args.get("date")
    
    res = db.get_doc(DB, config.testCol, name, age, date)
    return jsonify(res), 200

@app.route("/delete-doc", methods=["DELETE"])
def delete_doc():
    body = request.get_json()
    name = body.get("name")
    age = body.get("age")
    date = body.get("date")
    
    res = db.delete_doc(DB, config.testCol, name, age, date)
    return "Deleted", 200

def main():
    global DB
    DB = db.connect_db(config.host, config.db)
    app.run(host="0.0.0.0", port=9000, debug=True)


if __name__ == "__main__":
    main()