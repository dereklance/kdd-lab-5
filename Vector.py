import math
import os
from scipy import spatial

# Takes in a file with document path as the first line
# and then rows with columns labeled: term tfidf document_term_frequency
# and generates an object representation of these for comparing
class Vector:

	def __init__(self, document_path):
		self.tfidf_vector = []
		self.tfidf_vector_with_term = []
		self.term_frequencies = dict()

		with open(document_path, 'r') as input_file:
			self.document_size = os.path.getsize(document_path)
			line_num = 0
			for line in input_file:
				if line_num == 0:
					self.document_path = line
				elif line_num > 1:
					[term, tfidf, document_term_frequency] = line.split(" ")[:]
					self.tfidf_vector.append(tfidf)
					self.tfidf_vector_with_term.append((term, tfidf))
					self.term_frequencies[term] = document_term_frequency

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