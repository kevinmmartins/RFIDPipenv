#!/usr/bin/env python

import SimpleHTTPServer
import SocketServer
import RFID

PORT = 8000

class GetHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
	tag = RFID.read_serial()
        print tag
        self.wfile.write(tag)
        # self.send_response(200, 'OK')

Handler = GetHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
