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