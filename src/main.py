import os
from tornado.httpserver import HTTPServer 
from tornado.ioloop import IOLoop
from motor.motor_tornado import MotorClient
from dotenv import load_dotenv
from routes import router

load_dotenv()

if __name__ == "__main__":
  connection_string = os.environ['MONGO_CONNECTION_STRING']
  client = MotorClient(connection_string)
  db = client['denox']
  
  port = int(os.environ['API_PORT'])
  params = { 'db': db }

  server = HTTPServer(router(params))
  server.listen(port)
  print(f"Server up at http://localhost:{port} 🚀", flush=True)
  
  server.start(0)
  IOLoop.current().start()
