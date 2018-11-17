import sys
import pprint
import math
from Vector import Vector
from parser import parse_documents

def calculate_tf_idf(term, document_term_frequencies, total_term_frequencies, document_frequencies):
	tf = document_term_frequencies[term]
	df = document_frequencies[term]
	idf = math.log(len(total_term_frequencies) / df)

	return tf * idf

def main():
	data_directory = sys.argv[1]
	stop_words_filename = sys.argv[2]

	# Parse documents
	document_term_frequencies, total_term_frequencies, document_frequencies, \
		average_document_size = parse_documents(data_directory, stop_words_filename)

	# Create document_frequencies file
	with open(f"./output/document_frequencies.txt", "w") as output:
		output.write("term document_frequency\n")
		for term, frequency in document_frequencies.items():
			output.write(f'{term} {frequency}\n')

	# Create document specific term frequency files
	for document_path, term_frequencies in document_term_frequencies.items():
		[author, article] = document_path.split('/')[-2:]
		with open(f"./output/documents/" + article, "w") as output:
			output.write(f'{document_path} \n')
			output.write("term tf-idf document_term_frequency\n")

			for term, _ in total_term_frequencies.items():
				tfidf = calculate_tf_idf(term, term_frequencies, total_term_frequencies, document_frequencies)
				output.write(f'{term} {tfidf} {term_frequencies[term]}\n')

if __name__ == '__main__':
	main()