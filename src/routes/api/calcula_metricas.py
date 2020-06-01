import json
import time
from datetime import datetime
from pandas import DataFrame
from tornado.web import RequestHandler
from lib.movement import movement
from lib.centroids import calculate_centroids


date_template = "%d/%m/%Y %H:%M:%S %z"

def parse_date(date_string):
  return datetime.strptime(f'{date_string} -0300', date_template).strftime("%s")


class CalculaMetricas(RequestHandler):
  async def post(self):
    body = json.loads(self.request.body)
    serial = body['serial']
    datahora_inicio = parse_date(body['datahora_inicio'])
    datahora_fim = parse_date(body['datahora_fim'])
    
    query = {
      'serial': serial,
      'datahora': {
        '$gt': datahora_inicio,
        '$lt': datahora_fim
      }
    }
    pipeline = [
      { '$match': query },
      { '$sort': { 'datahora': 1 } }
    ]

    db = self.settings['db']
    dados_rastreamento = db['dados_rastreamento']

    cursor = dados_rastreamento.aggregate(pipeline)

    document_list = []
    async for document in cursor:
      document_list.append(document)
    df = DataFrame(document_list)

    data = movement(df)
    centers = calculate_centroids(df)

    response = {
      'distancia_percorrida': data['distance'],
      'tempo_em_movimento': data['moving'],
      'tempo_parado': data['still'],
      'centroides_paradas': centers.tolist(),
      'serial': serial
    }

    resultados = db['resultados_eduardo']
    resultados.insert_one(response)

    self.write(response)
