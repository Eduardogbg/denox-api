from tornado.web import Application
from .calcula_metricas import CalculaMetricas
from .retorna_metricas import RetornaMetricas

def api_app(path, params):
  app = Application([
    (f"{path}/calcula_metricas", CalculaMetricas),
    (f"{path}/retorna_metricas", RetornaMetricas)
  ])
  app.settings['db'] = params['db']
  
  return app
