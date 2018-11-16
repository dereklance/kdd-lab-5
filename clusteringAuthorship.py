from Vector import Vector, construct_vectors

def main():
  vectors = construct_vectors()
  for vector in vectors:
    print(vector.document_path)

if __name__ == "__main__":
    main()
    