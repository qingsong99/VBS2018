from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import search

class GP(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        print self.path
        print 'Get Request'
        search.process()

    def do_POST(self):
        print 'Post Request'
        search.process()

def run(server_class=HTTPServer, handler_class=GP, port=8088):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Server running at localhost:8088...'
    httpd.serve_forever()

run()

