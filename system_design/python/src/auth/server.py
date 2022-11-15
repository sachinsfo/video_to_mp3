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
    
    # check db for username and password
    cur = mysql.connection.cursor()
    res = cur.execute(
        'select email, password from user where email = %s', (auth.username,)
    )
    # user exists
    if res > 0:
        user_row = cur.fetchone()
        email, password = user_row

        if auth.username != email or auth.password != password:
            return 'Invalid credentials!', 401
        else:
            return createJWT(auth.username, os.environ.get('JWT_SECRET'), True)
    # user does not exist
    else:
        return 'Invalid credentials! User does not exist!', 401

def createJWT(username, secret, authz):
    return jwt.encode({
            username: username,
            exp: datetime.datetime.now(tz=datetime.timezone.utc)
                    + datetime.timedelta(days=1),
            iat: datetime.datetime.utcnow(),
            admin: authz
        }, 
        secret,
        algorithm='HS256'
    )
        
if __name__ == '__main__':
    srvr.run(host='0.0.0.0', port=5000)