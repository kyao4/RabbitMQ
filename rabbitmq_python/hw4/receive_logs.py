'''
Created on 2018年1月22日

@author: yaokai2
'''
import pika
import sys
 
def callback(ch, method, properties, body):
    print('received %r message %r' % (method.routing_key, body))
 
if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue
    severities = sys.argv[1:]
    if not severities:
        sys.stderr.write('Usage: [info] [warning] [error]\n')
        sys.exit(1)
     
    for severity in severities:
        channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=severity)
    print('[*] start consuming, to exit enter CTRL + C')
    channel.basic_consume(callback, queue=queue_name, no_ack=True)
     
    channel.start_consuming()
