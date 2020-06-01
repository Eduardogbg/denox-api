from tornado.httpserver import HTTPServer 
from tornado.ioloop import IOLoop
from pymongo import MongoClient
from routes import router

server = HTTPServer(router)

if __name__ == "__main__":
  port = 8892
  server.listen(port)
  print(f"Server up at http://localhost:{port} 🚀", flush=True)
  IOLoop.current().start()
