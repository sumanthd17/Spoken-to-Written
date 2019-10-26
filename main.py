from spoken2written import S2W

if __name__ == '__main__':
	# Input text
	# input_text = 'where is the P M O office'

	input_text = 'convert triple A to number. Where is the P M O office. convert two dollars to number'

	# Intializing the class
	s2w = S2W(input_text)

	output_text = s2w.driver()

	print("Input: ", input_text)
	print("Output: ", output_text)

	# Individual Features

	# output_text = s2w.findAbbreviation(input_text)
	# output_text = s2w.word2num(input_text)
	# output_text = s2w.combineAbbreviations(input_text)