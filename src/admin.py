import pika
from admin_message_pb2 import AdminCommand

def handle_message(channel, method, properties, body):
    command = AdminCommand()
    command.ParseFromString(body)
    print properties.reply_to
    
    channel.basic_publish(exchange='admin_exchange',
                          routing_key=properties.reply_to,
                          properties=pika.BasicProperties(correlation_id = properties.correlation_id),
                          body='Une reponse')
    channel.basic_ack(delivery_tag = method.delivery_tag)

def main():
    print "Starting server"
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.9.93'))
    channel = connection.channel()
    channel.queue_declare(queue='admin_queue')
    
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(handle_message, queue='admin_queue')
    
    print " [x] Awaiting requests"
    channel.start_consuming()
    
if __name__ == "__main__":
    main()