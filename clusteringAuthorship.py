from Vector import Vector
import glob
import sys

def main():
  vectors = []
  for vector_file_path in glob.glob("./output/*.txt"):
    vectors.append(Vector(vector_file_path))

  print(vectors)

if __name__ == "__main__":
    main()
    