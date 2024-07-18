from http.server import SimpleHTTPRequestHandler, HTTPServer

class RequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        print(f"Received GET request to: {self.path}")
        print(f"Headers: {self.headers}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Success')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        print(f"Received POST request to: {self.path}")
        print(f"Headers: {self.headers}")
        print(f"Body: {post_data.decode('utf-8')}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Success')

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd server on port {port}')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
