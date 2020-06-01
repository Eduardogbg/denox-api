from tornado.web import RequestHandler

class CalculaMetricas(RequestHandler):
  def get(self):
    self.write("Calcula")
