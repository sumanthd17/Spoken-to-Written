from spoken2written import S2W

if __name__ == '__main__':
	# Input text
	input_text = 'convert ten lakh dollars to number'

	# Intializing the class
	s2w = S2W(input_text)

	output_text = s2w.word2num()
	print("Input: ", input_text)
	print("Output: ", output_text)