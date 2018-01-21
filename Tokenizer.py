#########################################################################
# Assignment 4: Tokenizer.py
# Chloe Sheen
########################################################################
import string

# tokenizer takes a string and returns a list of the sentences contained in that string.
def tokenizer(text):
	end_punctuation = ['.','?'] # omitted : and ; as sentences do not end with those punctuations
	sentence = ''
	sentences = []
	months = ['Jan', 'Feb', 'Mar', 'Apr', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] # omit May
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

	for i in range(len(text)):
		if ((text[i] in end_punctuation) and
			# takes care of abbreviated first names
			(text[i-1] not in string.ascii_uppercase) and
			# takes care of month abbreviations
			(text[i-3:i] not in months) and
			# takes care of decimal points, years, cents. 1977 exception, then make new sentence
			# precondition for index to not go out of range
			((i < len(text)-1 and text[i+1] not in numbers) or i == len(text)-1)):
				sentence+=text[i]
				sentences.append(sentence)
				sentence = ''

		elif ((text[i] in end_punctuation) and (i < len(text)-1 and text[i+1] == '"')):
			if text[i] is '!':
				sentence+=text[i]
				sentences.append(sentence)
				sentence = ''

		else:
			sentence += text[i]
	return sentences

# print_sentences takes a list of strings and prints them one at a time
def print_sentences(sentence_list):
	i = 1
	for s in sentence_list:
		print 'Sentence',i,':',s
		i+=1

# Demonstration: rewrite demo() so that it
# 1) opens the file tokenizertest.txt and reads it into a string,
# 2) sends that string to tokenizer,
# 3) sends the result of tokenizer to print_sentences,
# 4) closes the file tokenizertest.txt

def demo():
	with open('tokenizertest.txt', 'r') as f:
		input = f.read().replace('\n','')
		res = tokenizer(input)
		print_sentences(res)
		f.close()

if __name__=='__main__':
	demo()
