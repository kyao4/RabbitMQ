'''
Created on 2018年2月1日

@author: yaokai2
'''

import requests
import json



def getTraceFiles(host, port, username, password):
    status = 404
    traces = []
    counter = 1
    while (status != 200 or len(traces) == 0):
        r = requests.get('http://%s:%s/api/trace-files' % (host, port), auth=(username, password))
        status = r.status_code
        traces = r.json()
        print("tried %s times" % counter)
        counter += 1
        if counter > 15:
            break
    return traces

def getTraceFile(host, port, username, password, filename='test_log.txt'):
    status = 404
    traces = []
    counter = 1
    while (status != 200 or len(traces) == 0):
        r = requests.get('http://%s:%s/api/trace-files/%s' % (host, port, filename), auth=(username, password))
        status = r.status_code
        traces = r.json()
        print("tried %s times" % counter)
        counter += 1
        if counter > 15:
            break
    return traces


def getTraces(host, port, username, password, vhost='%2f', name=''):
    status = 404
    traces = []
    counter = 1
    while (status != 200 or len(traces) == 0):
        r = requests.get('http://%s:%s/api/traces/%s/%s' % (host, port, vhost, name), auth=(username, password))
        status = r.status_code
        traces = r.json()
        print("tried %s times" % counter)
        counter += 1
        if counter > 15:
            break
    return traces


def putTrace(host, port, username, password, vhost='%2f', name='', trace_format='text', pattern="#", max_payload_bytes=1000):
    status = 404
    count = 1
    while(status != 201):
        r = requests.put('http://%s:%s/api/traces/%s/%s' % (host, port, vhost, name), 
                         data= json.dumps({"format": trace_format,
                                "pattern": pattern, 
                                "max_payload_bytes": max_payload_bytes}), 
                         auth=(username, password), 
                         headers = {'content-type': 'application/json'})
        status = r.status_code
        print(count, status)
        count += 1
        if count > 15:
            if status == 400:
                print(r.json())
            return False
    return True

def deleteTrace(host, port, username, password, vhost='%2f', name=''):
    status = 404
    count = 1
    while(status != 204):
        r = requests.delete('http://%s:%s/api/traces/%s/%s' % (host, port, vhost, name), auth=(username, password)) 
        status = r.status_code
        print(count, status)
        count += 1
        if count > 15:
            print(r.json())
            return False
    return True


if __name__ == '__main__':
    
    '''
    GET            /api/traces
    GET            /api/traces/<vhost>
    GET PUT DELETE /api/traces/<vhost>/<name>
    GET            /api/trace-files
    GET     DELETE /api/trace-files/<name>    (GET returns the file as text/plain)
    '''
    
#     tracesFiles = getTraceFiles('10.99.206.217', 8004, 'admin', 'admin')
#     print(tracesFiles)
     
#     traces = getTraces('10.99.206.217', 8004, 'admin', 'admin', vhost='%2fvhost_poc', name='')
#     print(traces)

#     status = putTrace('10.99.206.217', 8004, 'admin', 'admin', vhost='%2fvhost_poc', name="tracing_task_queue_publisher", pattern="#.")
#     print(status)
#     status = deleteTrace('10.99.206.217', 8004, 'admin', 'admin', vhost='%2fvhost_poc', name="tracing_task_queue_publisher")
#     print(status)



