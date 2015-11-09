#! /usr/bin/env python
# coding: utf-8

import CGIHTTPServer
import BaseHTTPServer
import cgitb

class Handler(CGIHTTPServer.CGIHTTPRequestHandler):
  cgi_directories = ["/cgi-bin"]

# use debug
cgitb.enable()

PORT = 8888

httpd = BaseHTTPServer.HTTPServer(
  ("", PORT),
  Handler
)

print "serving at port", PORT

httpd.serve_forever()
