import sys
import os
import re
from collections import defaultdict

def get_author_accuracy(cluster):
  max_count = 0
  max_author = None
  total_count = 0
  cluster_counts = defaultdict(int)
  for author, count in cluster.items():
    total_count += count
    cluster_counts[author] = count
    if count > max_count:
      max_author = author
      max_count = count

  return max_author, max_count, total_count, cluster_counts

def main():

  cluster_author_counts = dict()
  author_hits_misses = dict()
  cluster_num = None
  accuracies = []

  with open("clusterOutput.txt", "r") as input:
    for line in input:
      if "Cluster" in line:
        if cluster_num:
          max_author, max_count, total_count, author_counts = \
            get_author_accuracy(cluster_author_counts[cluster_num])
          accuracy = max_count / total_count
          accuracies.append(accuracy)
          for author, count in author_counts.items():
            current_author_hit_misses = author_hits_misses[author] if author in author_hits_misses else (0, 0)
            if author == max_author:
              author_hits_misses[author] =  (current_author_hit_misses[0] + author_counts[author], 0)
            else:
              author_hits_misses[author] =  (0, current_author_hit_misses[1] + author_counts[author])
          print("Cluster " + str(cluster_num))
          print("Author Prediction: " + max_author)
          print("Accuracy: " + str(max_count) + "/" + str(total_count) + " " + str(accuracy * 100) + "%")
          print()
          
        cluster_num = int(re.split(" |:", line)[1])
        cluster_author_counts[cluster_num] = defaultdict(int)
      else:
        [author, article] = line.split('/')[-2:]
        cluster_author_counts[cluster_num][author] += 1

  if cluster_num:
    max_author, max_count, total_count, author_counts = \
      get_author_accuracy(cluster_author_counts[cluster_num])
    accuracy = max_count / total_count
    accuracies.append(accuracy)
    for author, count in author_counts.items():
      current_author_hit_misses = author_hits_misses[author]
      if author == max_author:
        author_hits_misses[author] = current_author_hit_misses + (author_counts[author], 0)
      else:
        author_hits_misses[author] = current_author_hit_misses + (0, author_counts[author])
    print("Cluster " + str(cluster_num))
    print("Author Prediction: " + max_author)
    print("Accuracy: " + str(max_count) + "/" + str(total_count) + " " + str(accuracy * 100) + "%")
    print()
      
  else:
    [author, article] = line.split('/')[-2:]
    cluster_author_counts[cluster_num][author] += 1

  print("Author accuracies:")
  for author, hit_misses in author_hits_misses.items():
    print(author + ": " + str(((hit_misses[0] + 1) / (hit_misses[0] + hit_misses[1] + 1)) * 100) + "%")

  print("\nTotal Accuracy: " + str(sum(accuracies) / len(accuracies) * 100) + "%")

if __name__ == "__main__":
  main()
