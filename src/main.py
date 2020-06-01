from tornado.httpserver import HTTPServer 
from tornado.ioloop import IOLoop
from motor.motor_tornado import MotorClient
from routes import router


if __name__ == "__main__":
  client = MotorClient('mongodb://user:secret@localhost:27019/')
  db = client['denox']
  
  port = 8892
  params = { 'db': db }

  server = HTTPServer(router(params))
  server.listen(port)
  print(f"Server up at http://localhost:{port} 🚀", flush=True)
  
  server.start(0)
  IOLoop.current().start()
