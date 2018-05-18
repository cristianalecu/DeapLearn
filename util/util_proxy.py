import os
def set_proxy():
    proxy_addr = 'http://{user}:{passwd}@{address}:{port}'.format(
        user='cna', passwd='5tyuiop[]', 
        address='192.168.1.29', port=int('8080'))
    os.environ['http_proxy'] = proxy_addr
    os.environ['https_proxy'] = proxy_addr

def unset_proxy():
    os.environ.pop('http_proxy')
    os.environ.pop('https_proxy')