import pika
import traceback
import threading


def print_message(channel, method, properties, body):
    print 'RECEIVED:' + body
    data = body.split('@')
    print data[0] + ' says:' + data[1] 

def listening(user_name, channel):
    print "Registering to " + user_name
    result = channel.queue_declare(exclusive=True)
    channel.queue_bind(exchange='imessage', queue=result.method.queue, routing_key=user_name)
    channel.basic_consume(print_message, queue=result.method.queue, no_ack=True)
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
if __name__ == "__main__":
    main()