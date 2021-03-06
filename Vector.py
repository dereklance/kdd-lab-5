import math
import os
import glob
import csv
from sys import stdout
from scipy import spatial

# Takes in a file with document path as the first line
# and then rows with columns labeled: term tfidf document_term_frequency
# and generates an object representation of these for comparing
class Vector:
	def __init__(self, document_path):
		self.tfidf_vector = []
		self.tfidf_vector_with_term = []
		self.tfidf_dict = dict()
		self.term_frequencies = dict()

		with open(document_path, 'r') as input_file:
			self.document_size = os.path.getsize(document_path)

			csvreader = csv.reader(input_file, delimiter=' ')
			self.document_path = next(csvreader, None)[0] # Get path
			self.author_name = self.document_path.split('/')[2]
			next(csvreader, None) # Skip header line

			for [term, tfidf, document_term_frequency] in csvreader:
				self.tfidf_vector.append(float(tfidf))
				self.tfidf_vector_with_term.append((term, float(tfidf)))
				self.term_frequencies[term] = document_term_frequency

				if float(tfidf) > 0:
					self.tfidf_dict[term] = round(float(tfidf), 3)

	def __str__(self):
		return f'{self.tfidf_dict}\n{self.author_name}'

	@staticmethod
	def cosine_similarity(vector1, vector2):
		return 1 - spatial.distance.cosine(vector1.tfidf_vector, vector2.tfidf_vector)

	@staticmethod
	def okapi(vector1, vector2, average_size, k1, b, k2, n, document_frequencies):
		okapi_sum = 0
		for i in range(len(vector1.tfidf_vector)):
			term = vector1.tfidf_vector_with_term[i][0]
			okapi_sum += (
				math.log((n - document_frequencies[term] + 0.5) / 
							   (document_frequencies[term] + 0.5))
				*
				(((k1 + 1) * vector1.term_frequencies[term]) / 
				 (k1 * (1 - b + b * (vector1.document_size / average_size) + vector1.term_frequencies[term])))
				*
				(((k2 + 1) * vector2.term_frequencies[term]) / 
				 (k2 + vector2.term_frequencies[term]))
			)
		return okapi_sum

# Use limit for testing purposes only
def construct_vectors(limit = None):
	vectors = []
	print("Constructing vectors...")
	files = glob.glob("./output/documents/*.txt")
	for i, vector_file_path in enumerate(files):
		stdout.write(f"\rProgress: {(i)}/{len(files)}")
		stdout.flush()
		vectors.append(Vector(vector_file_path))
		if limit and i >= limit:
			break
	stdout.write("\nDone\n")
	return vectors

def write_vectors_to_file(file_name):
	vectors = construct_vectors()

	with open(file_name, 'w') as output_file:
		for vector in vectors:
			for term, tfidf in vector.tfidf_dict.items():
				output_file.write(f'{term.strip("-")}:{tfidf} ')
			output_file.write(f'__AUTHOR__:{vector.author_name}\n')

def main():
	write_vectors_to_file('document_vectors.txt')

if __name__ == '__main__':
	main()