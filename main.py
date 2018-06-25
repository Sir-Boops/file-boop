import magic
import mimetypes
from http.server import HTTPServer, BaseHTTPRequestHandler

base_path = 'C:\\Users\\admin\\basic-workspace\\file-boop\\'

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        # If /
        if self.path == '/index.html':
            self.path = '/'

        # If it's just the index just return boop
        if self.path == '/':
            self.send_response(200)
            resp = bytes('Boop!', "utf8")
            self.send_header('Content-type', magic.from_buffer(resp, mime=True))
            self.end_headers()
            self.wfile.write(resp)

        else:
            try:
                file = (base_path + (self.path.split('/')[len(self.path.split('/')) - 1]))
                request_file = open(file, 'rb').read()
                self.send_response(200)
                self.send_header('Content-type', magic.from_file(file, mime=True))

            except:
                request_file = bytes('Not found!', "utf8")
                self.send_response(404)
                self.send_header('Content-type', magic.from_buffer(request_file, mime=True))

            self.end_headers()

            self.wfile.write(request_file)

        return

def run():
    httpd = HTTPServer(('127.0.0.1', 7777), Serv)
    httpd.serve_forever()

run()
