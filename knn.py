import math, sys

def euclidianDistance(pointA, pointB):
	set_of_keys = set(pointA.keys() + pointB.keys())
	differences = pointA.get()

def addNeighbor(neighbors, distanceToAdd, neighborToAdd):
	neighbors.pop()
	if distanceToAdd >= neighbors[len(neighbors) - 1][0]:
		neighbors.append((distanceToAdd, neighborToAdd))
		return distanceToAdd
	for index, (distance, neighbor) in enumerate(neighbors):
		if distanceToAdd < distance:
			neighbors.insert(index, (distanceToAdd, neighborToAdd))
			return neighbors[len(neighbors) - 1][0]

def knn(data, k):
	predictions = []

	for toClassifyIndex, pointToClassify in enumerate(data):
		nearestNeighbors = [(sys.maxsize, None)] * k
		maxNeighbor = sys.maxsize
		for index, dataPoint in enumerate(data):
			if index != toClassifyIndex:
				distance = euclidianDistance(pointToClassify, dataPoint)
				if distance < maxNeighbor:
					maxNeighbor = addNeighbor(nearestNeighbors, distance, dataPoint)
		classifications = [neighbor['__AUTHOR__'] for _, neighbor in nearestNeighbors]
		predictions.append(max(set(classifications), key=classifications.count))
	return predictions

def main():
	print('knn running')

if __name__ == '__main__':
	main()