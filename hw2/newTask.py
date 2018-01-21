'''
Created on 2018年1月20日

@author: kyao4
'''


import pika
import sys 
connection = pika.BlockingConnection(pika.ConnectionParameters(host='loacalhost'))
channel = connection.channel()
channel.queue_declare(queue="task_queue", durable=True)
message = ' '.join(sys.argv[1:]) or "Hello, world"
channel.basic_publish(exchange=' ', routing_key='task_queue', body=message
                      , properties=pika.BasicProperties(delivery_mode=2))
print("[x] sent %r" % message)
connection.close()