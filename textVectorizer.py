import sys
from parser import parse_documents

def main():
	data_directory = sys.argv[1]
	output_filename = sys.argv[2]
	stop_words_filen = sys.argv[3]

	total_word_counts, document_word_counts = \
		parse_documents(data_directory, stop_words_filen)

	print(len(total_word_counts))
	print(len(document_word_counts))


if __name__ == '__main__':
	main()