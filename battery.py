PORT = 8001

cmd = "pmset -g batt | grep Internal  | cut -f 2"

from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse, subprocess

def battery():
    s = subprocess.check_output(cmd, shell=True)
    a = s.split("%")
    b = a[1].split(";")[1]
    return a[0]+"\n"+b.strip()


class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(battery())

httpd = HTTPServer(("", PORT), GetHandler)
httpd.serve_forever()


