import sys
from parser import parse_documents

def main():
	data_directory = sys.argv[1]
	output_filename = sys.argv[2]
	stop_words_filen = sys.argv[3]

	total_term_frequencies, document_term_frequencies, document_frequencies = \
		parse_documents(data_directory, stop_words_filen)

	print(len(total_term_frequencies))
	print(len(document_term_frequencies))
	print(len(document_frequencies))


if __name__ == '__main__':
	main()