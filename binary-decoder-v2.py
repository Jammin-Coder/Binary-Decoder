#!/usr/bin/python3

###########################
# Binary Decoder V2
# Jammin Coder
# 2/17/2021
###########################


binary_number = input("Enter a binary number >> ")


# This function creates a list of column values that will be used to decode the number
def create_column_values(binary_num):
    values = []  # Holds the column values
    n = 1  # This is the number that keeps track of the value that each column holds. Always starts at 1.

    for _ in binary_num:
        '''
        For the length of the binary number, insert the value of n into the first index.
        Then n is doubled.
        If the binary number's length is 4, then the resulting list will look like:
        [8, 4, 2, 1]
        '''
        values.insert(0, n)
        n *= 2
    return values


def evaluate_binary_number(binary_num, column_values):
    total = 0
    for i in range(0, len(binary_num)):
        '''
        This loops over each index of the binary number and checks 
        if it's equal to 1. If it is, then the corresponding
        value in column_values is added to total.
		
        i.e 
        binary_num = "1010"
        column_values = [8, 4, 2, 1]
        "1  0  1  0"
        [8, 4, 2, 1]
        
        1 over the 8, 1 over the 2. Nothing over the 4 or 1. So...
        8 + 2 = 10
		
    	##############################
		binary_num = "1111"
		column values are the same as before since the binary number is still 4 digits long.
		
        "1  1  1  1"
        [8, 4, 2, 1]
        
        1 over the 8, 1 over the 3, 1 over the 2, 1 over the 1. So...
        8 + 4 + 2 + 1 = 15  
        '''
        if binary_num[i] == str(1):
            total += column_values[i]
    return str(total)


values = create_column_values(binary_number)
base10_num = evaluate_binary_number(binary_number, values)
print("Decoded num >> " + base10_num)
