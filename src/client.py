import pika
import traceback
import threading
import time


def print_message(channel, method, properties, body):
    print 'RECEIVED:' + body
    data = body.split('@')
    print data[0] + ' says:' + data[1] 

def listening(user_name, channel):
    print "Registering to " + user_name
    result = channel.queue_declare(exclusive=True)
    channel.queue_bind(exchange='nfc_central', queue=result.method.queue, routing_key=user_name)
    channel.basic_consume(print_message, queue=result.method.queue, no_ack=True)
    channel.start_consuming()

def main():
    user_name = raw_input('User name:')
    print "Hello " + user_name
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.9.93'))
    channel = connection.channel()
    try:
        channel.exchange_declare(exchange='nfc_central', type='direct')
    except:
        print "Exchange already exists or some error!"
        traceback.print_exc()
        print "**************************************"
    channel.basic_publish(exchange='nfc_central', routing_key='registering', body=user_name + '@hashtag')
    
    listener = threading.Thread(target=listening, args = (user_name, channel))
    listener.start()
    
    data = raw_input(">")
    while data!='quit':
        if '@' in data:
            target = data.split('@')[0]
            message = data.split('@')[1]
            print 'sending to ' + target + ' -> [' + message + ']'
            channel.basic_publish(exchange='nfc_central', routing_key=target, body=user_name + '@' + message)
        data = raw_input(">")
        
    channel.basic_publish(exchange='nfc_central', routing_key='unregistering', body=user_name + '@hashtag')
    listener._Thread__stop()
    time.sleep(1)
    
if __name__ == "__main__":
    main()