from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

PORT = int(os.environ.get("PORT", 8080))

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(os.path.abspath(__file__)), **kwargs)

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Server running on port {PORT}")
    server.serve_forever()
