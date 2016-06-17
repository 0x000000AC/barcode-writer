# barcode maker.py
# A program for drawing code 128A barcodes

# Each character in the barcode symbol is composed of three bars and three spaces
# The stop adds an additional extra bar of length 2.
# ASCII value 0 can be viewed as 10011101100, where a 1 (one) is a
# bar and a 0 is a space. A single 1 would be the thinnest line in
# the bar code. Three 1 (111) in sequence indicates a bar three times as thick 
# as a single 1 bar

# The specification for Code 128 (ISO/IEC 15417) leaves the maximum length 
# undefined and states that this is something that should be defined by any 
# derivative application[*] standard. GS1-128 (the formal application of 
# Code 128 to the supply chain industry) limits it to 48 characters for example.

import argparse # Used to take cmd line arguments
import time # Used in main program to pause program before exit
import turtle   # Used in your function to print the bar code

SLEEP_TIME = 8 # number of seconds to sleep after drawing the barcode, probably could be done another way
# Encodings are for 128A, incomplete at the moment more here: https://en.wikipedia.org/wiki/Code_128
ENCODINGS_DICT = {' ': '11011001100', '!': '11001101100', '"': '11001100110', '#': '10010011000',
	'$': '10010001100', '%': '10001001100', '&': '10011001000', "'": '10011000100'}

# TO DO: function for start/stop bits and FNC
# 11010000100 start 
# 1100011101011 stop
# 11110101110 FNC

# TO DO: function for check sequence
# The checksum digit is based on a modulo 103 calculation 
# based on the weighted sum of the values of each of the
# digits in the message that is being encoded, including the start character.

def draw_bar(my_turtle, binString):
	my_turtle.pensize(3)
	for item in binString:
		if '1' in item:
			my_turtle.left(90)
			my_turtle.forward(80)
			my_turtle.up()
			my_turtle.backward(80)
			my_turtle.right(90)
			my_turtle.forward(3)
			my_turtle.down()
		else:		
			my_turtle.left(90)
			my_turtle.up()
			my_turtle.forward(80)
			my_turtle.backward(80)
			my_turtle.right(90)
			my_turtle.forward(3)
			my_turtle.down()
				
def encode_alphaNum(my_turtle, word, binString):  
	for alphaNum in str(word):
		if ENCODINGS_DICT.has_key(alphaNum):
			binString += (ENCODINGS_DICT.get(alphaNum))
		else:
			print ("Character value not found " + str(alphaNum))
		
	print ("This is the encoded string: " + binString)
	draw_bar(my_turtle, binString)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("WORD", type=str)
	args = parser.parse_args()
	word = args.WORD
	my_turtle = turtle.Turtle()
	binString = ''
	# I think around 44 charachters is a bit much, so I may change later
	# to a smaller amount of chars so scanners can read it.
	if len(word) > 0 and len(word) < 44:
		encode_alphaNum(my_turtle, word, binString)
	else:
		exit(0)
	time.sleep(SLEEP_TIME)

if __name__ == "__main__":
    main()

