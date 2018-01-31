'''
Created on 2018年1月22日

@author: kyao4
'''

import pika
import sys

if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
    routing_key = sys.argv[1] if len(sys.argv) >= 2 else 'anonymous.info'
    message = ' '.join(sys.argv[2:]) or 'hello, world'
    channel.basic_publish(exchange='topic_logs', routing_key=routing_key, body=message)
    print("[x] sent one message %r with routing key %r" % (message, routing_key))
    connection.close()
    