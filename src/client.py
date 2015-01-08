import pika
import traceback
import threading
from admin_message_pb2 import AdminCommand, AdminControl
import uuid

callback_queue = None

def handle_admin_request(channel, method, properties, body):
    print body

def wait_admin_request(channel):
    channel.basic_consume(handle_admin_request, no_ack=True, queue=callback_queue)
    
def send_admin_request(channel, request):
    corr_id = str(uuid.uuid4())
    channel.basic_publish(exchange='',
                    routing_key='admin_queue',
                    properties=pika.BasicProperties(
                        reply_to = callback_queue,
                        correlation_id = corr_id,
                    ),
                    body=request.SerializeToString())
def print_message(channel, method, properties, body):
    print 'RECEIVED:' + body
    data = body.split('@')
    print data[0] + ' says:' + data[1] 

def listening(user_name, channel):
    result = channel.queue_declare(exclusive=True)
    channel.queue_bind(exchange='imessage', queue=result.method.queue, routing_key=user_name)
    channel.basic_consume(print_message, queue=result.method.queue, no_ack=True)
    channel.start_consuming()

def main():
    user_name = raw_input('User name:')
    
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.9.93'))
    channel = connection.channel()
    
    admin_control = AdminControl()
    admin_control.authentication_key = 'This is moi the user -> ' + user_name
    admin_request = AdminCommand()
    admin_request.user = user_name
    admin_request.command = 'login'
    admin_request.control.MergeFrom(admin_control)
    result = channel.queue_declare(exclusive=True)
    callback_queue = result.method.queue
    admin = threading.Thread(target=wait_admin_request, args = (channel,))
    admin.start()
    
    send_admin_request(channel, admin_request)
    
    admin.join()
    
    print "Hello " + user_name
    
    
    try:
        channel.exchange_declare(exchange='imessage', type='direct')
    except:
        print "Exchange already exists or some error!"
        traceback.print_exc()
        print "**************************************"
    listener = threading.Thread(target=listening, args = (user_name, channel))
    listener.start()
    data = raw_input(">")
    while data!='quit':
        if '@' in data:
            target = data.split('@')[0]
            message = data.split('@')[1]
            print 'sending to ' + target + ' -> [' + message + ']'
            channel.basic_publish(exchange='imessage', routing_key=target, body=user_name + '@' + message)
        data = raw_input(">")
    listener._Thread__stop()
    admin._Thread_stop()
if __name__ == "__main__":
    main()