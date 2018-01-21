import httplib

c = httplib.HTTPConnection('localhost', 8088)
c.request('POST', '/return', '{}')
