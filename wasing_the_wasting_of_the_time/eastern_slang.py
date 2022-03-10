from multiprocessing.sharedctypes import Value
import sys

if len(sys.argv) < 2:
	print("\n\teastern_slang.py needs a string to read:\neastern_slang.py \"sentence\" -file <filename> \n")
	exit()

# for i,arg in enumerate(sys.argv):
# 	print(i,arg)


try:
	filename = sys.argv[sys.argv.index('-file')+1]
except ValueError:
	filename = None
except IndexError:
	print("filename not provided")
	filename = None

if sys.argv[1] != '-file':
	sentence = sys.argv[1]
else: sentence = None

print('loading spacy')
import spacy
nlp = spacy.load("en_core_web_md")

# from nltk import pos_tag
# from nltk.tokenize import word_tokenize, sent_tokenize
print('done')

# def find_root(sent):
def create_sentence(word):
	ising_of_the_new = ''
	print(f'{word}, {word.lemma_}')
	if word.pos_ == 'VERB':
		if word.lemma_ == 'be':
			ising_of_the_new += str(word) + "ing "
		else:
			ising_of_the_new += word.lemma_ + "ing "
	elif word.pos_ == 'NOUN':
		if word.lemma_.lower() not in ['i', 'me', 'mine', 'the']:
			ising_of_the_new += "of the " + word.lemma_ + " of the "
	
	for child in word.children:
		print(child)
		ising_of_the_new += create_sentence(child)
	return ising_of_the_new
	

if sentence:
	print(f'translating sentence: {sentence}')
	
	doc = nlp(sentence)
	for sent in doc.sents:
		ising_of_the_new = ''
		for token in sent:
			print(f'{str(token):12} {str(token.lemma_):10} {str(token.pos_):10} {str(token.head):10}')
		print()
		ising_of_the_new = create_sentence(sent.root)
		print(ising_of_the_new)


	







if filename:
	print(f'translating file: {filename}')
	# try:
	# 	file = open(filename)
	# 	text = file.read()
	# 	file.close()
	# except:
	# 	print("failed to read file. exiting")
	# 	exit()
	file = open(filename)
	text = file.read()
	doc = nlp(text)
	for sent in doc.sents:
		ising_of_the_new = ''
		for token in sent:
			print(f'{str(token):12} {str(token.lemma_):10} {str(token.pos_):10} {str(token.head):10}')
		print()
		ising_of_the_new = create_sentence(sent.root)
		print(ising_of_the_new)
