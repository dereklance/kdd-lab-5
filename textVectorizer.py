import sys
import pprint
from Vector import Vector
from parser import parse_documents

def main():
	data_directory = sys.argv[1]
	output_filename = sys.argv[2]
	stop_words_filename = sys.argv[3]

	# Parse documents
	document_term_frequencies, total_term_frequencies, document_frequencies, \
		average_document_size = parse_documents(data_directory, stop_words_filename)

	# Construct Vector objects
	vectors = dict()
	for document, term_frequencies in document_term_frequencies.items():
		vectors[document] = Vector(term_frequencies, total_term_frequencies, document_frequencies)

	# Output vector objects to files
	for document, vector in vectors.items():
		split_filename = document.split('.')
		output_filename = split_filename[0] + '-out.' + split_filename[1]

		with open('./output/' + output_filename, 'w') as output:
			for term, idf_df in vector.vector_space.items():
				output.write(f'{term} {idf_df}\n')

if __name__ == '__main__':
	main()