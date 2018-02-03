'''
Created on 2018年2月3日

@author: yaokai2
'''

import pika

def callback(ch, method, properties, body):
    print("received log, payload: %s" % body)
    

if __name__ == '__main__':
    credentials=pika.PlainCredentials('admin', 'admin')
    conn = pika.BlockingConnection(pika.ConnectionParameters(host='10.99.206.217', port=5672, virtual_host='/vhost_poc', credentials=credentials))
    channel = conn.channel()
    result = channel.queue_declare()
    queue_name = result.method.queue
    channel.queue_bind(queue=queue_name, exchange='amq.rabbitmq.trace', routing_key='#')
    print("start consuming, waiting for new logs")
    channel.basic_consume(callback, queue=queue_name, no_ack=True)
    channel.start_consuming()