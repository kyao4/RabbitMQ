'''
Created on 2018年1月20日

@author: kyao4
'''


import pika
import sys 
credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.99.206.217', port=5672, virtual_host="/vhost_poc",  credentials=credentials))
channel = connection.channel()
channel.queue_declare(queue="task_queue_kai", durable=True)
message = ' '.join(sys.argv[1:]) or "Hello, world"
channel.basic_publish(exchange='', routing_key='task_queue_kai', body=message
                      , properties=pika.BasicProperties(delivery_mode=2))
print("[x] sent %r" % message)
connection.close()
