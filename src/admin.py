import pika
import traceback
import threading
import time
import NFCentral

def print_message(channel, method, properties, body):
    print 'RECEIVED:' + body
    data = body.split('@')
    print data[0] + ' says:' + data[1]
    
def listening_registering(working_queue, channel, server_status):
    print "Registering thread"
    channel.queue_bind(exchange='nfc_central', queue=working_queue.method.queue, routing_key="registering")
    channel.basic_consume(server_status.add_user, queue=working_queue.method.queue, no_ack=True)
    channel.start_consuming()
    
def listening_unregistering(working_queue, channel, server_status):
    print "Unregistering thread"
    channel.queue_bind(exchange='nfc_central', queue=working_queue.method.queue, routing_key="unregistering")
    channel.basic_consume(server_status.remove_user, queue=working_queue.method.queue, no_ack=True)
    channel.start_consuming()
    
def listening_query(working_queue, channel, server_status):
    print "Query thread"
    channel.queue_bind(exchange='nfc_central', queue=working_queue.method.queue, routing_key="query")
    channel.basic_consume(print_message, queue=working_queue.method.queue, no_ack=True)
    channel.start_consuming()

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.9.93'))
    channel = connection.channel()
    try:
        channel.exchange_declare(exchange='nfc_central', type='direct')
    except:
        print "Exchange already exists or some error!"
        traceback.print_exc()
        print "**************************************"
    working_queue = channel.queue_declare(exclusive=True)
    listeners = [listening_registering, listening_unregistering, listening_query]
    listening_functions = []
    server_status = NFCentral.Users()
    for listener in listeners:
        listener_function = threading.Thread(target=listener, args = (working_queue, channel, server_status))
        listener_function.start()
        listening_functions.append(listener_function)
        time.sleep(1)

    data = raw_input(">")
    while data!='quit':
        data = raw_input(">")
        
    for listening_function in listening_functions:
        listening_function._Thread__stop()
        time.sleep(1)
    
if __name__ == "__main__":
    main()