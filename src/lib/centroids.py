from pandas import DataFrame
from sklearn.cluster import KMeans

def calculate_centroids(df):

  still_list = []
  for index, row in df.iterrows():
    if not row['situacao_movimento']:
      still_list.append([row['latitude'], row['longitude']])

  array = DataFrame(still_list).to_numpy()
  kmeans = KMeans(n_clusters=len(still_list), random_state=0).fit(array)

  return kmeans.cluster_centers_
