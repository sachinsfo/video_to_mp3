import os, gridfs, pika, json
from flask import Flask, request
from flask_pymongo import PyMongo
from auth import validate
from auth_svc import access
from storage import util

srvr = Flask(__name__)
srvr.config["MONGO_URI"]="mongodb://host.minikuber.internal:27017/videos"

mongo = PyMongo(srvr)

fs = gridfs.GridFS(mongo.db)

# Makes connection to RabbitMQ synchronous
conn = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
channel = conn.channel()

@srvr.route('/login', methods=['POST'])
def login():
    token, err = access.login(request)
    if not err:
        return token
    else:
        return err

@srvr.route('/upload', methods=['POST'])
def upload():
    access, err = validate.token(request) 
    access = json.loads(access)
    if access["admin"]:
        if len(request.files) != 1:
            return "Exactly 1 file is required.", 400
        
        for _, f in request.files.items():
            err = util.upload(f, fs, channel, access)
            if err:
                return err
        
        return "File upload successful!", 200
    else:
        return "User not an admin! Unauthorized!", 401
            
@srvr.route('/download', methods=['GET'])
def download():
    pass

if __name__ == "__main__":
    srvr.run(host="0.0.0.0", port=8080)