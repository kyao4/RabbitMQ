'''
Created on 2018年1月21日

@author: kyao4
'''
import pika

def callback(ch, method, properties, body):
    print(" [x] %r" % body)
   


if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='logs', exchange_type='fanout')
    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange='logs', queue=queue_name)
    print('[*] waiting for logs, to exit press CTRL + C')
    channel.basic_consume(callback, queue=queue_name, no_ack=True)
    channel.start_consuming()