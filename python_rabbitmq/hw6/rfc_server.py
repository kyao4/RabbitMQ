'''
Created on 2018年1月23日

@author: yaokai2
'''

import pika
import uuid

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def on_request(ch, method, props, body):
    n = int(body)
    print('[*] fib(%s)' % body)
    response = fib(n)
    ch.basic_publish(exchange='', routing_key=props.reply_to, 
                     properties=pika.BasicProperties(correlation_id= \
                                                     props.correlation_id), 
                     body=str(response))
    ch.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='rfc_queue')
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(on_request, queue='rfc_queue')
    print("waiting RFC request")
    channel.start_consuming()
    
    