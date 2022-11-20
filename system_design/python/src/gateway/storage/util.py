import pika, json

'''
f => File the user is trying to upload
fs => GridFS instance
chanel => RabbitMQ channel
access => User's access
'''
def upload(f, fs, channel, access):
    fid, err = put_file_in_db(fs, f)
    if not fid:
        return "Internal Server Error. File Upload Failed. Err = {err}", 500

    msg, err = create_message(fid, access)
    if not msg:
        return "Internal Server Error. Message Creation Failed. Err = {err}", 500
    
    rsp, err = enqueue_message(fs, fid, channel, msg)
    if not rsp:
        return "Internal Server Error. Unable To Enqueue The File to RabbitMQ. Err = {err}", 500
    
    print('Video is enqueued successfully!')

def put_file_in_db(fs, f):
    try:
        fid = fs.put(f) 
        return fid, None

    except Exception as e:
        return None, e

def create_message(fid, access):
    try:
        message = {
            "video_fid": str(fid),
            "mp3_fid": None,
            "username": access["username"]
        }
        return message, None

    except Exception as e:
        return None, e

def enqueue_message(fs, fid, channel, message):
    try:
        # When exchange is Empty, our routing_key becomes the queue name
        # Here, we have two queues in our RabbitMQ, 1. video queue 2. mp3 queue
        channel.basic_publish(
            exchange = '',
            routing_key = 'video',
            body = json.dumps(message),
            properties = pika.BasicProperties(
                # If our k8 pod crashes, we want our messages to be persisted in the queue
                delivery_mode = pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
        return True, None

    except Exception as e:
        # If we can't place the file in the queue, we must delete it from our database (mongodb)
        fs.delete(fid)
        return None, e
        
