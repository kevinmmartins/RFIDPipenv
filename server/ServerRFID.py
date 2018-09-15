#!/usr/bin/env python

import SimpleHTTPServer
import SocketServer
import RFID
import traceback
import json

class GetHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        try:
            tag = RFID.read_serial()
            print tag
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
    PORT = 8000
    Handler = GetHandler
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    print "Serving at port ",PORT
    httpd.serve_forever()

if __name__ == "__main__":
    main()
