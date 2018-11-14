from pathlib import Path
from collections import Counter
import sys

def parseDocuments(dataDirectory):
	filePaths = (str(path) for path in Path(dataDirectory).glob('**/*.txt'))
	summedCounts = Counter()

	with open('groundTruths.txt', 'w') as outputFile:
		for path in filePaths:
			[author, article] = path.split('/')[-2:]
			outputFile.write(f'{article},{author}\n')
			
			with open(path, 'r') as document:
				tokens = document.read().split()
				tokens = list(map(lambda token: token.strip(',"()[]<>?.{}+=`~').lower(), tokens))
				summedCounts += Counter(tokens)
		
		print(len(summedCounts))

def main():
	dataDirectory = sys.argv[1]

	parseDocuments(dataDirectory)

if __name__ == '__main__':
	main()