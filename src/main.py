from sklearn.cluster import DBSCAN
import numpy as np
from random import random
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
from sklearn.metrics.pairwise import haversine_distances

def generate_points(center, no_points):
    points = []
    for _ in range(no_points):
        lat = random()
        lon = random()
        new_point = [center[0] + lat, center[1] + lon]
        points.append(new_point)
        
    return points

def convert_radians_to_km(radians):
  R = 6371
  return radians * R


def cluster_points(points):
  radians = np.radians(points)
  distances = convert_radians_to_km(haversine_distances(radians))

  dbscan = DBSCAN(eps=MAX_RADIUS, min_samples=1, metric='precomputed')
  preds = dbscan.fit_predict(distances)

  clusters = {}
  for i, label in enumerate(preds):
      if label not in clusters:
          clusters[label] = []
      clusters[label].append(points[i])

  return clusters

def print_clusters(clusters):
  print("Number of clusters: ", len(clusters.keys()))
  geolocator = Nominatim(user_agent="my_application")

  # Print the points in each cluster
  for label, cluster_points in clusters.items():
      print("Cluster", label, "contains", len(cluster_points))
      for point in cluster_points:
        location = geolocator.reverse(str(point[0]) + "," + str(point[1]))
        print(point, "location:", location.address)

if __name__ == "__main__":
    MAX_RADIUS = 1 # in KM unit
    NO_POINTS = 1000
    CENTER = [41.113224, 29.0191758]

    points = generate_points(CENTER, NO_POINTS)
    clusters = cluster_points(points)

    print_clusters(clusters)


