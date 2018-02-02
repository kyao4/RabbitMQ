'''
Created on 2018年1月20日

@author: kyao4
'''
import pika
import time
def callback(ch, method, properties, body):
    print(" [x] received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] done.")
    ch.basic_ack(delivery_tag=method.delivery_tag)

if __name__ == '__main__':
    credentials = pika.PlainCredentials('admin', 'admin')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.99.206.217', port=5672, virtual_host="/vhost_poc", credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue="task_queue_kai", durable=True)
    print(" [*] waiting for message, press CTRL + C to exit")
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(callback, queue="task_queue_kai")
    channel.start_consuming()
