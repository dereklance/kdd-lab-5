import math

class Vector:

	def __init__(self, term_frequencies, total_term_frequencies, document_frequencies):
		self.term_frequencies = term_frequencies
		self.total_term_frequencies = total_term_frequencies
		self.document_frequencies = document_frequencies

		self.vector_space = self.compute_vector_space()

	def compute_vector_space(self):
		vector_space = dict()
		for term, _ in self.term_frequencies.items():
			vector_space[term] = self.calculate_tf_idf(term)
		return vector_space

	def calculate_tf_idf(self, term):
		df = self.document_frequencies[term]
		idf = math.log(len(self.total_term_frequencies) / df)

		return df * idf

	def cosine_similarity(self, other_vector):
		return 0

	def okapi(self, other_vector):
		return 1