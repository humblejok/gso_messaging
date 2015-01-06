import pika
import traceback
import threading


def print_message(channel, method, properties, body):
    data = body.split('@')
    print data[0] + ' says:' + data[1] 

def listening(user_name, channel):
    channel.queue_bind(exchange='imessage', queue='all_messages', routing_key=user_name)
    channel.basic_consume(print_message, queue='all_messages', no_ack=True)
    channel.start_consuming()

def main():
    user_name = raw_input('User name:')
    print "Hello " + user_name
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.9.93'))
    channel = connection.channel()
    try:
        channel.exchange_declare(exchange='imessage', type='direct')
    except:
        print "Exchange already exists or some error!"
        traceback.print_exc()
        print "**************************************"
    try:
        channel.queue_declare(queue='all_messages', exclusive=True)
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
            print 'sending to ' + target 
            channel.basic_publish(exchange='imessage', routing_key=target, body=data)
        data = raw_input(">")
    listener._Thread__stop()
if __name__ == "__main__":
    main()