import sys

def gather_digit(filesname):
	array, files = [], open(filesname)
	for lines in files:
		lists = lines.rstrip().split()
		for i in range(len(lists)):
			word = lists[i]
			for j in range(len(word)):
				if word[j].isdigit() == True:
					array.append(word[j])
		return ''.join(array)
	files.close()

def gather_lower(filesname):
	array, files = [], open(filesname)
	for lines in files:
		lists = lines.rstrip().split()
		for i in range(len(lists)):
			word = lists[i]
			for j in range(len(word)):
				if word[j].islower() == True:
					array.append(word[j])
		return ''.join(array)
	files.close()

def gather_upper(filesname):
	array, files = [], open(filesname)
	for lines in files:
		lists = lines.rstrip().split()
		for i in range(len(lists)):
			word = lists[i]
			for j in range(len(word)):
				if word[j].isupper() == True:
					array.append(word[j])
		return ''.join(array)
	files.close()

def gather_upper_digit(filesname):
	array, files = [], open(filesname)
	for lines in files:
		lists = lines.rstrip().split()
		for i in range(len(lists)):
			word = lists[i]
			for j in range(len(word)):
				if word[j].isupper() == True or word[j].isdigit() == True:
					array.append(word[j])
		return ''.join(array)
	files.close()

if __name__ == '__main__':
	filesname = sys.argv[1]
	print(gather_digit(filesname))
	print(gather_lower(filesname))
	print(gather_upper(filesname))
	print(gather_upper_digit(filesname))