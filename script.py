data_directory = 'C50'

file_paths = (str(path) for path in Path(data_directory).glob('**/*.txt'))

with open('groundTruths.txt', 'w') as outputFile:
	for path in file_paths:
		[author, article] = path.split('/')[-2:]
		outputFile.write(f'{article},{author}\n')