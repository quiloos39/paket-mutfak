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


def cluster_points(points, max_radius):
  radians = np.radians(points)
  distances = convert_radians_to_km(haversine_distances(radians))

  dbscan = DBSCAN(eps=max_radius, min_samples=1, metric='precomputed')
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


def elbow_method(points):
    results = []
    for i in range(1, 21):
        kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=1)
        kmeans.fit(points)
        results.append(kmeans.inertia_)

    plt.plot(range(1, 21), results)
    plt.title("The Elbow Method (optimized distance)")
    plt.xlabel("Number of clusters")
    plt.show()

if __name__ == "__main__":
    MAX_RADIUS = 1 # in KM unit
    NO_POINTS = 1000
    CENTER = [41.113224, 29.0191758]

    points = generate_points(CENTER, NO_POINTS)
    clusters = cluster_points(points, MAX_RADIUS)
    elbow_method(points)
    
    print_clusters(clusters)


