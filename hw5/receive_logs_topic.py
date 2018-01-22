'''
Created on 2018年1月22日

@author: kyao4
'''

import pika
import sys

def callback(ch, method, properties, body):
    print("[*] received message %r with routing key %r" % (body, method.routing_key))

if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue
    '''
    Topic exchange 并不意味着只可以绑定一个routing key，你也可以给一个queue绑定多个routing key
    别忘了给参数输入添加错误提示处理
    '''
    routing_keys = sys.argv[1:]
    if not routing_keys:
        sys.stderr.write('usage: [source.severity]')
        sys.exit(1)
    for key in routing_keys:
        '''
        binding 是queue 和 exchange 的绑定，所以叫做queue_bind
        '''
        channel.queue_bind(queue=queue_name, exchange="topic_logs", routing_key=key)
    channel.basic_consume(callback, queue=queue_name, no_ack=True)
    print("[*] waiting for logs, To exit press CTRL + C")
    channel.start_consuming()
    