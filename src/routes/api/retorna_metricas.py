from tornado.web import RequestHandler

class RetornaMetricas(RequestHandler):
  async def get(self):
    db = self.settings['db']
    resultados = db['resultados_eduardo']

    cursor = resultados.find({})

    self.write(await cursor.to_list(length=100))