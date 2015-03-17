import nltk, re, pprint
import numpy as np
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

def spacing(lines):
	for i in range(0,lines):
		print
		if i == lines-1:
			print "---------------------------------------------------------"

def get_column(records, col_index, separator=','):

	column = []
	for line in records:
		tokens = line.split(separator)
		if col_index < len(tokens):
			token = tokens[col_index].strip()
		else:
			token = ''
		column.append(token)

	return column


spacing(5);

p = open('city_and_the_sky_full.txt', 'Ur')
memory = p.read()


pos = {}
wt = word_tokenize(memory)
pos = pos_tag(wt)

# for line in pos:
# 	if 'NNS' in line:
# 		print line[0]

# for line in pos:
# 	if 'JJ'	in line:
# 		print line[0]

for line in pos:
	if 'VBZ' in line:
		print line[0]

for line in pos:
	if 'VBP' in line:
		print line[0]

for line in pos:
	if 'VBN' in line:
		print line[0]

for line in pos:
	if 'VB' in line:
		print line[0]


# for line in pos:
# 	print line


