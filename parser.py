from pathlib import Path
from collections import Counter, defaultdict
from porterStemmer import PorterStemmer
import sys

def strip_word(word):
	return word.strip(',"()[]<>?.{}+=`~\n').lower()

def get_stop_words(path):
	stop_words = set()
	with open(path, 'r') as stop_words_file:
		for word in stop_words_file:
			stop_words.add(strip_word(word))

	return stop_words

def stemmed(word):
	return PorterStemmer().stem(word, 0, len(word) - 1)

def parse_documents(data_directory, stop_words_file):
	file_paths = (str(path) for path in Path(data_directory).glob('**/*.txt'))
	stop_words = get_stop_words(stop_words_file)

	total_term_frequencies = defaultdict(int)
	document_frequencies = defaultdict(int)
	all_document_term_frequencies = dict() # of total_term_frequencies like dicts

	with open('groundTruths.txt', 'w') as outputFile:
		for path in file_paths:
			[author, article] = path.split('/')[-2:]
			outputFile.write(f'{article},{author}\n')
			
			with open(path, 'r') as document:
				visited_terms = set()
				document_term_frequencies = defaultdict(int)
				for token in document.read().split():
					token = strip_word(token) # Strip unecessary punctuation
					if not (token in stop_words): # Remove stop words
						token = stemmed(token) # Apply stemming
						
						# Compute document frequencies
						if not token in visited_terms:
							document_frequencies[token] += 1
							visited_terms.add(token)

						document_term_frequencies[token] += 1
						total_term_frequencies[token] += 1

				all_document_term_frequencies[article] = document_term_frequencies

	return all_document_term_frequencies, total_term_frequencies, document_frequencies