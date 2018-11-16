from Vector import Vector, construct_vectors
from hclustering import utility_main

def main():
  vectors = construct_vectors(100)
  dataset = [vector.tfidf_vector for vector in vectors]
  utility_main(dataset, 20)

if __name__ == "__main__":
    main()
    