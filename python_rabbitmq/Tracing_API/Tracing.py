'''
Created on 2018年2月1日

@author: yaokai2
'''

import requests
import json
if __name__ == '__main__':
    
    '''
    GET            /api/traces
    GET            /api/traces/<vhost>
    GET PUT DELETE /api/traces/<vhost>/<name>
    GET            /api/trace-files
    GET     DELETE /api/trace-files/<name>    (GET returns the file as text/plain)
    '''
    url_visit = 'http://10.99.206.217:8004/api/trace-files'
    r = requests.get('http://10.99.206.217:8004/api/traces', auth=('admin', 'admin'))
#     print(r.status_code)
#     print(r.json())
    
#     r = requests.put('http://10.99.206.217:8004/api/traces/%2fvhost_poc/test_api_tracing_kai', 
#                      data= json.dumps({"format":"text",
#                             "pattern":"deliver.task_queue_kai", 
#                             "max_payload_bytes":1000}), 
#                      auth=('admin', 'admin'), 
#                      headers = {'content-type': 'application/json'})
#     print(r.status_code)
#     print(r.json())
    r = requests.delete('http://10.99.206.217:8004/api/traces/%2fvhost_poc/test_api_tracing_kai', auth=('admin', 'admin'))
    print(r.status_code)