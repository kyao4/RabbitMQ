'''
Created on 2018年2月1日

@author: yaokai2
'''

import requests

if __name__ == '__main__':
    
    '''
    GET            /api/traces
    GET            /api/traces/<vhost>
    GET PUT DELETE /api/traces/<vhost>/<name>
    GET            /api/trace-files
    GET     DELETE /api/trace-files/<name>    (GET returns the file as text/plain)
    '''
    url_visit = 'http://10.99.206.217:8004/api/trace-files'
    r = requests.get('http://10.99.206.217:8004/api/traces/vhost_poc', auth=('admin', 'admin'))
    print(r.status_code)
    print(r.json())
