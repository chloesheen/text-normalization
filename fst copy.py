#############################################################################################
# Chloe Sheen
# FST object class
# Resources: https://stackoverflow.com/questions/14229643/python-reading-a-tab-separated-file-using-delimiter
#############################################################################################
from string import lowercase

class Transducer:
	def __init__ (self, final=1):
		self.state = 0
		self.final = final
		self.transition = {}
		self.output = ""		# this time, we need to keep track of the output string

	# adds transition specifying start, end, and string if "accepting" passes
	# initially .extend, using .append now: https://stackoverflow.com/questions/2022031/
	# python-append-vs-operator-on-lists-why-do-these-give-different-results
	def addTransition(self, startState, endState, alpha, alphaOutput):
		if alpha in lowercase:
			self.transition[(startState, alpha)] = [endState, alphaOutput]  # keeping track of output string
			return True
		return False

	def getTransition(self, alpha, state):
		if (state, alpha) in self.transition:
			return self.transition[(state, alpha)]
		else:
			return [False, ""]   	# because it will be unpacked into 2

	# sets the final state
	def setFinal(self, state):
		if state is not self.final: self.final = state

	# runs the string through the FST
	def execute(self, string):
		if not isinstance(string, str):
			# str is not string
			print "Not a string."
			return False

		for c in string:
			transition, tempOutput = self.getTransition(c, self.state)		# unpack
			if not transition is False:
				self.state = transition
				self.output += tempOutput	# add temp output to output
			else:
				print "Input string '" + str(string) + "' is not accepted."
				return False

		if self.state == self.final:
			print "%s outputs %s" % (string, self.output)
			return True
		else:
			print "%s outputs %s" % (string, self.output)
			return False

	def demo(self):
		"""
		INITIAL DEMO from #2: demo of my program, returns the string you gave it except when it sees the first 'a', outputs 'b'
		for i in ["c", "abab", "bbbbbb", "aaa", "abaab", "bababa", "baa", "A", "a1", "!a", "ab?!"]:
			fst = Transducer()
			fst.setFinal(1)
			fst.addTransition(0,1, "a", "b")
			fst.addTransition(0,0, "b", "b")
			fst.addTransition(1,1, "a", "a")
			fst.addTransition(1,1, "b", "b")

			fst.execute(i)
		"""
		with open('minidictionary.txt', 'r') as f:
			# splitting file with tabs as delimiters:
			# https://stackoverflow.com/questions/14229643/python-reading-a-tab-separated-file-using-delimiter
			word_list=[]
			for line in f:
				word_list.append(line.strip().split("\t"))

			for i in range(len(word_list)):
				lenlist = []
				"""
				Attempt at making one FST to pass all, but couldn't carry out separately for all cases...
				for c in range(0,13):

					ffst = Transducer()
					ffst.setFinal(lenlist[c])

					str_len = len(word_list[l][0])
					lenlist.append(str_len)

					for j in range(0,lenlist[c]):
						ffst.addTransition(j, j+1, word_list[1][0][j], word_list[1][1][2*j:2*j+2])
				"""
				for c in range(0,13):
					str_len = len(word_list[c][0])
					lenlist.append(str_len)

				fst = Transducer()
				fst.setFinal(lenlist[0])
				for j in range(0,lenlist[0]):
					fst.addTransition(0, 1, word_list[0][0][0], word_list[0][1][0:3])
					fst.addTransition(j, j+1, word_list[0][0][j], word_list[0][1][2*j+1:2*j+3])

				fst2 = Transducer()
				fst2.setFinal(lenlist[1])
				for j in range(0,lenlist[1]):
					fst2.addTransition(j, j+1, word_list[1][0][j], word_list[1][1][2*j:2*j+2])

				fst3 = Transducer()
				fst3.setFinal(lenlist[2])
				for j in range(0,lenlist[2]):
					fst3.addTransition(j, j+1, word_list[2][0][j], word_list[2][1][2*j:(2*j)+2])

				fst4 = Transducer()
				fst4.setFinal(lenlist[3])
				for j in range(0,lenlist[3]):
					fst4.addTransition(j, j+1, word_list[3][0][j], word_list[3][1][2*j:(2*j)+2])

				fst5 = Transducer()
				fst5.setFinal(lenlist[4])
				for j in range(0,lenlist[4]):
					fst5.addTransition(j, j+1, word_list[4][0][j], word_list[4][1][2*j:(2*j)+2])

				fst6 = Transducer()
				fst6.setFinal(lenlist[5])
				for j in range(0,lenlist[5]):
					fst6.addTransition(j, j+1, word_list[5][0][j], word_list[5][1][2*j:(2*j)+2])

				fst7 = Transducer()
				fst7.setFinal(lenlist[6])
				for j in range(0,lenlist[6]):
					fst7.addTransition(j, j+1, word_list[6][0][j], word_list[6][1][2*j:(2*j)+2])

				fst8 = Transducer()
				fst8.setFinal(lenlist[7])
				for j in range(0,lenlist[7]):
					fst8.addTransition(j, j+1, word_list[7][0][j], word_list[7][1][2*j:(2*j)+2])

				fst9 = Transducer()
				fst9.setFinal(lenlist[8])
				for j in range(0,lenlist[8]):
					fst9.addTransition(j, j+1, word_list[8][0][j], word_list[8][1][2*j:(2*j)+2])

				fst10 = Transducer()
				fst10.setFinal(lenlist[9])
				for j in range(0,lenlist[9]):
					fst10.addTransition(j, j+1, word_list[9][0][j], word_list[9][1][2*j:(2*j)+2])

				fst11 = Transducer()
				fst11.setFinal(lenlist[10])
				for j in range(0,lenlist[10]):
					fst11.addTransition(j, j+1, word_list[10][0][j], word_list[10][1][2*j:(2*j)+2])

				fst12 = Transducer()
				fst12.setFinal(lenlist[11])
				for j in range(0,lenlist[11]):
					fst12.addTransition(0, 1, word_list[11][0][0], word_list[11][1][0:3])
					fst12.addTransition(j, j+1, word_list[11][0][j], word_list[11][1][2*j+1:(2*j)+3])

				fst13 = Transducer()
				fst13.setFinal(lenlist[12])
				for j in range(0,lenlist[12]):
					fst13.addTransition(0, 1, word_list[12][0][0], word_list[12][1][0:3])
					fst13.addTransition(j, j+1, word_list[12][0][j], word_list[12][1][2*j+2:(2*j)+4])

			# for u in range(0,13):
				# ffst.execute(str(word_list[u][0]))
			fst.execute(str(word_list[0][0]))
			fst2.execute(str(word_list[1][0]))
			fst3.execute(str(word_list[2][0]))
			fst4.execute(str(word_list[3][0]))
			fst5.execute(str(word_list[4][0]))
			fst6.execute(str(word_list[5][0]))
			fst7.execute(str(word_list[6][0]))
			fst8.execute(str(word_list[7][0]))
			fst9.execute(str(word_list[8][0]))
			fst10.execute(str(word_list[9][0]))
			fst11.execute(str(word_list[10][0]))
			fst12.execute(str(word_list[11][0]))
			fst13.execute(str(word_list[12][0]))

# Python doesn't have "Main"?: http://python.berkeley.edu/events/assets/newbie_nugget_Oct2_2013.html
if __name__ == '__main__':
	acc = Transducer()
	acc.demo()
