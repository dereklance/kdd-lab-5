import sys
import os
import re
from collections import defaultdict

def get_author_accuracy(cluster):
  max_count = 0
  max_author = None
  total_count = 0
  for author, count in cluster.items():
    total_count += count
    if count > max_count:
      max_author = author
      max_count = count

  return max_author, max_count, total_count

def main():

  cluster_author_counts = dict()
  cluster_num = None
  accuracies = []

  with open("clusterOutput.txt", "r") as input:
    for line in input:
      if "Cluster" in line:
        if cluster_num:
          max_author, max_count, total_count = \
            get_author_accuracy(cluster_author_counts[cluster_num])
          accuracy = max_count / total_count
          accuracies.append(accuracy)
          print("Cluster " + str(cluster_num))
          print("Author Prediction: " + max_author)
          print("Accuracy: " + str(max_count) + "/" + str(total_count) + " " + str(accuracy * 100) + "%")
          print()
          
        cluster_num = int(re.split(" |:", line)[1])
        cluster_author_counts[cluster_num] = defaultdict(int)
      else:
        [author, article] = line.split('/')[-2:]
        cluster_author_counts[cluster_num][author] += 1

  print("Total Accuracy: " + str(sum(accuracies) / len(accuracies)))

if __name__ == "__main__":
  main()
