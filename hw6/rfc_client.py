'''
Created on 2018年1月23日

@author: yaokai2
'''
import pika
import uuid

class FibonacciRpcClient():
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(exclusive=True)
        self.queue_name = result.method.queue
        '''
        这里客户端接受到response 以后不需要再ack, 要使用basic consume
        '''
        self.channel.basic_consume(self.on_response, no_ack=True, queue=self.queue_name)

    def on_response(self, ch, method, props, body):
        if self.correlation_id == props.correlation_id:
            self.response = body
    
    def call(self, n):
        self.response = None
        '''
        correaltion_id 要设置为实例变量
        '''
        self.correlation_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange = '', 
                                   routing_key='rfc_queue', 
                                   body=str(n), 
                                   properties=pika.BasicProperties(reply_to=self.queue_name, 
                                                        correlation_id=self.correlation_id))
        while self.response is None:
            '''
            这里用的是connection 对象
            '''
            self.connection.process_data_events()
        return int(self.response)
        
if __name__ == '__main__':
    client = FibonacciRpcClient()
    print("calling RFC with n: %d" % 4)
    result = client.call(4)
    print("Got %d" % result)
    