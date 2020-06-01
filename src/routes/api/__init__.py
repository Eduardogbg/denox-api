from tornado.web import Application
from .calcula_metricas import CalculaMetricas
from .retorna_metricas import RetornaMetricas

def api_app(path):
  return Application([
    (f"{path}/calcula_metricas", CalculaMetricas),
    (f"{path}/retorna_metricas", RetornaMetricas)
  ])
