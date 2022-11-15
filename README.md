# video_to_mp3
Python, Kubernetes, RabbitMQ, MongoDB, mySQL

# Source
https://www.youtube.com/watch?v=hmkF77F9TLw

# Install mysql using homebrew
- `brew install mysql`
- And run `mysql -u root` 

# Virtual Environment
- To create => `python3 -m venv venv`
- To activate => `source ./venv/bin/activate`
- To check => `env | grep VIRTUAL`

# Database schema
- auth (database)
- user (table) 

# Create database and tables 
- `mysql -u root < init.sql`

# Drop user and database
- `mysql -u root -e 'drop user auth_user@localhost;'`
- `mysql -u root -e 'drop database auth;'`

# Error -  Can`t connect to local MySQL server through socket 
- Solution: Kill the mysql and mysqld processes
- Run `brew services start mysql` to start mysql
- `brew services stop mysql` to stop mysql
- References:
    - https://stackoverflow.com/a/26460819
    - https://superuser.com/a/1413818

# Error - Command '/usr/bin/clang' failed with exit code 1
- This error occurred when I ran `pip3 install flask_mysqldb`
- Solution:
    - https://stackoverflow.com/a/72391553
    - `pip3 install --upgrade pip`
    - `python3 -m pip install --upgrade setuptools`
    - And then run `pip3 install flask_mysqldb` 

# Error - legacy-install-failure
- This error originates from a subprocess, and is likely not a problem with pip.
- Solution: Install xcode, and it works `xcode-select --install`