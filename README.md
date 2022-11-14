# video_to_mp3
Python, Kubernetes, RabbitMQ, MongoDB, mySQL

# Source
https://www.youtube.com/watch?v=hmkF77F9TLw

# Install mysql using homebrew
- `brew install mysql`
- And run `mysql -u root` 

# Error -  Can`t connect to local MySQL server through socket 
- Solution: Kill the mysql and mysqld processes
- Run `brew services start mysql` to start mysql
- `brew services stop mysql` to stop mysql
- References:
    - https://stackoverflow.com/a/26460819
    - https://superuser.com/a/1413818

# Virtual Environment
- To create => `python3 -m venv venv`
- To activate => `source ./venv/bin/activate`
- To check => `env | grep VIRTUAL`