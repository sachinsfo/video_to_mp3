import jwt, datetime, os
from flask import Flask, request
from flask_mysqldb import MySQL

srvr = Flask(__name__)
mysql = MySQL(srvr)

# config
srvr.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
srvr.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
srvr.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
srvr.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')
srvr.config['MYSQL_PORT'] = os.environ.get('MYSQL_PORT')

@srvr.route('/login', methods=["POST"])
def login():
    auth = request.authorization
    if not auth:
        return "Missing credentials", 401
    # else:
    #     auth.username
    #     auth.password
