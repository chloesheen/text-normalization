#########################################################################
# Assignment 4: fileio.py
# Chloe Sheen
# Sources: https://docs.python.org/2/library/fileinput.html
########################################################################
import string

def text_counter():
	chars = 0
	lines = 0
	words = 0
	w_result = []
	with open('test.txt', 'r') as f:
		for line in f:
			lines += 1
			chars += len(line)         # length of line
			words_list = line.split()
			words = len(words_list)    # split up the lines into words, and then count
			w_result.append(words)

		f_result = []
		for i in range (0,6):
			l_result = "Line %d has %d words. " % (i, w_result[i])
			f_result.append(l_result)

		result = "This file has %d characters. \nThis file has %d lines. \n" % (chars, lines)
		f.seek(0)
		f.close()

	with open('Sheen.txt', 'w') as o:
		o.write(result)
		for j in range(0,6):
			o.write(f_result[j])
			o.write("\n")

if __name__ == "__main__":
	text_counter()
