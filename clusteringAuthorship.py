from Vector import Vector, construct_vectors
from kmeans import utility_main
from sklearn.cluster import KMeans
import numpy

def main():
  vectors = construct_vectors()
  dataset = [vector.tfidf_vector for vector in vectors]

  with open("vectors.txt", "w") as output:
    for i, vector in enumerate(dataset):
      output.write(f"{len(vector)} {vectors[i].document_path}\n")
    
  kmeans = KMeans(n_clusters=50).fit(dataset)

  clusters = {i: numpy.where(kmeans.labels_ == i)[0] for i in range(kmeans.n_clusters)}
  with open("clusterOutput.txt", "w") as output:
    for i in range(len(clusters)):
      output.write(f"Cluster {i}:\n")
      for index in clusters[i]:
        output.write(f"{vectors[index].document_path}\n")

if __name__ == "__main__":
    main()
    