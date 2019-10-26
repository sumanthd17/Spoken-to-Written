from spoken2written import S2W

if __name__ == '__main__':
	# Input text
	input_text = 'where is the P M O office'

	# input_text = 'convert three to number'

	# Intializing the class
	s2w = S2W(input_text)

	# output_text = s2w.word2num()
	output_text = s2w.combineAbbreviations()
	print("Input: ", input_text)
	print("Output: ", output_text)