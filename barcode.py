# barcode maker.py

# function to make the barcode 
# or function to some intermediary like binary or ascii ?

# function to take in information from barcode scanner
# and make it into text

# take user input with in boundries
# call function to make the barcode
import argparse
import time # Used in main program to pause program before exit
import turtle   # Used in your function to print the bar code

## Constants used by this program
SLEEP_TIME = 30 # number of seconds to sleep after drawing the barcode
ENCODINGS = [[1, 1, 0, 0, 0],   # encoding for '0'
         [0, 0, 0, 1, 1],   # encoding for '1'
         [0, 0, 1, 0, 1],   # encoding for '2'
         [0, 0, 1, 1, 0],   # encoding for '3'
         [0, 1, 0, 0, 1],   # encoding for '4'
         [0, 1, 0, 1, 0],   # encoding for '5'
         [0, 1, 1, 0, 0],   # encoding for '6'
         [1, 0, 0, 0, 1],   # encoding for '7'
         [1, 0, 0, 1, 0],   # encoding for '8'
         [1, 0, 1, 0, 0]    # encoding for '9'
        ]
SINGLE_LENGTH = 25  # length of a short bar, long bar is twice as long

'''
def compute_check_digit(digits):

    sum = 0
    for i in range(len(digits)):
        sum = sum + digits[i]
    check_digit = 10 - (sum % 10)
    if (check_digit == 10):
        check_digit = 0
    return check_digit
'''

def draw_bar(my_turtle, digit):
    my_turtle.left(90)
    if digit == 0:
        length = SINGLE_LENGTH
    else:
        length = 2 * SINGLE_LENGTH
    my_turtle.forward(length)
    my_turtle.up()
    my_turtle.backward(length)
    my_turtle.right(90)
    my_turtle.forward(10)
    my_turtle.down()


def draw_zip(my_turtle, zip):  
	for str_digit in str(zip):
		digit = int(str_digit)
		for bar_bit in ENCODINGS[digit]:
			draw_bar(my_turtle, bar_bit)
			

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("ZIP", type=int)
    args = parser.parse_args()
    zip = args.ZIP
    if zip <= 0 or zip > 99999:
        print("zip must be > 0 and < 100000; you provided", zip)
    else:
        my_turtle = turtle.Turtle()
        draw_zip(my_turtle, zip)
        time.sleep(SLEEP_TIME)

if __name__ == "__main__":
    main()

