'''
Created on 2018年1月21日

@author: kyao4
'''

import pika
import sys

if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel=connection.channel()
    channel.exchange_declare(exchange="logs", exchange_type="fanout")
    message = ''.join(sys.argv[1:]) or "info: logs!!"
    channel.basic_publish(exchange="logs", routing_key='', body=message)
    print("[x] emit message %r" % message)
    connection.close()