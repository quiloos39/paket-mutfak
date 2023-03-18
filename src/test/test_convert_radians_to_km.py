import numpy as np
from main import cluster_points, convert_radians_to_km
from sklearn.metrics.pairwise import haversine_distances

def test_cluster_points():
  """ 
  Check that all points in each cluster are within 1 km
  """
  test_points = [[41.113224, 29.0191758], [41.113453, 29.019527], [41.114453, 29.021527], [41.115453, 29.023527]]
  clusters = cluster_points(test_points)
  
  for label in clusters:
      for point in clusters[label]:
          for other_point in clusters[label]:
              if point is not other_point:
                  radians = np.radians([point, other_point])
                  distance = convert_radians_to_km(haversine_distances(radians))
                  assert distance <= 1, f"Points {point} and {other_point} in cluster {label} are farther than 1 km apart."
