#!/usr/bin/env python

import SimpleHTTPServer
import SocketServer
from RFID import Rfid
import traceback
import json

class GetHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    
    def setup(self):
        self.request.settimeout(2)
        SimpleHTTPServer.SimpleHTTPRequestHandler.setup(self)

    def do_GET(self):
        try:
            print "Request received"
            rfid= Rfid()
            tag = rfid.read_serial()
            print tag
            rfid.close_serial()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'RFID': tag}))
        except:
            print "Unexpected error: " + traceback.format_exc()
            self.send_response(500)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

def main():
    try:
        PORT = 8766
        Handler = GetHandler
        httpd = SocketServer.TCPServer(("", PORT), Handler)
        print "Serving at port ",PORT
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print "Server stopped"

if __name__ == "__main__":
    main()
