import math
import os
from scipy import spatial

# Basically just takes in dictionaries of term frequencies for a 
# specific document, as well as total term frequencies, and document frequencies
# and creates a tf-idf vector from it for a given file.
# Also has static methods for comparing vectors.
class Vector:

	def __init__(self, document_path, term_frequencies, total_term_frequencies, document_frequencies):
		self.document_path = document_path
		self.document_size = os.path.getsize(self.document_path)
		self.term_frequencies = term_frequencies
		self.total_term_frequencies = total_term_frequencies
		self.document_frequencies = document_frequencies

		self.vector_space = self.compute_vector_space()
		self.vector = [value for key, value in self.vector_space.items()]

	def compute_vector_space(self):
		vector_space = dict()
		for term, _ in self.total_term_frequencies.items():
			vector_space[term] = self.calculate_tf_idf(term)
		return vector_space

	def calculate_tf_idf(self, term):
		tf = self.term_frequencies[term]
		df = self.document_frequencies[term]
		idf = math.log(len(self.total_term_frequencies) / df)

		return tf * idf

	@staticmethod
	def cosine_similarity(vector1, vector2):
		return 1 - spatial.distance.cosine(vector1.vector, vector2.vector)

	@staticmethod
	def okapi(vector1, vector2, average_size, k1, b, k2):
		okapi_sum = 0
		for i in range(len(vector1.vector)):
			term = vector1.vector_space.items()[i][0]
			okapi_sum += (
				math.log((len(vector1.vector) - vector1.document_frequencies[term] + 0.5) / 
							   (vector1.document_frequencies[term] + 0.5))
				*
				(((k1 + 1) * vector1.term_frequencies[term]) / 
				 (k1 * (1 - b + b * (vector1.document_size / average_size) + vector1.term_frequencies[term])))
				*
				(((k2 + 1) * vector2.term_frequencies[term]) / 
				 (k2 + vector2.term_frequencies[term]))
			)
		return okapi_sum