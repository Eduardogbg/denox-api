from tornado.web import RequestHandler

class RetornaMetricas(RequestHandler):
  def get(self):
    self.write("Retorna")
