from math import pi, sin, cos, atan2, sqrt

radius = 6371e3 # meters

def dist(lat1, lat2, lon1, lon2):
  delta_phi = lat2 - lat1
  delta_lambda = lon1 - lon2

  haver = (sin(delta_phi/2)**2) + cos(lon1)*cos(lon2)*(sin(delta_lambda/2)**2)
  c = 2 * atan2(sqrt(haver), sqrt(1 - haver))

  return radius * c

def movement(df):
  total_still = 0
  total_moving = 0
  total_distance = 0

  last_time = 0
  was_still = False
  last_lat = 0
  last_lon = 0

  for index, row in df.iterrows():
    time = row['datahora']
    is_moving = row['situacao_movimento']
    lat = row['latitude'] * pi/180
    lon = row['longitude'] * pi/180

    if (last_time != 0):
      delta = time - last_time
      if (was_still):
        total_still += delta
      else:
        total_moving += delta
      
      total_distance += dist(last_lat, lat, last_lon, lon)
    
    last_time = time
    was_still = is_moving
    last_lat = lat
    last_lon = lon

  return {
    'moving': total_moving,
    'still': total_still,
    'distance': total_distance
  }
