import sys, knn, Vector

def parse_vector_document(vector_document):
	document_vectors = dict()
	with open(vector_document) as file:
		lines = file.read().split('\n')
		for index, line in enumerate(lines):
			dict_items = line.split()
			for item in dict_items:

				x = item.split(':')
				if len(x) != 2:
					print(index + 1, x)
				# document_vectors[key] = value
	return document_vectors
		

def output_predicted_authorship_to_file(vector_document, k, similarity_function):
	vectors = parse_vector_document(vector_document)
	print(vectors[0:10])

def main():
	vector_document = sys.argv[1]
	k = int(sys.argv[2])
	similarity_metric = sys.argv[3]

	if similarity_metric == 'cosine':
		output_predicted_authorship_to_file(vector_document, k, Vector.Vector.cosine_similarity)
	elif similarity_metric == 'okapi':
		output_predicted_authorship_to_file(vector_document, k, Vector.Vector.okapi)
	else:
		raise ValueError('Argument 3 must be either \'cosine\' or \'okapi\'')

if __name__ == '__main__':
	main()