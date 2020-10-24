#!/usr/env/bin/ python3

#################################
# Binary To Base 10 Decoder, v1.1
# Made by TeknoBen96
# 10/24/2020, 1:40 P.M
#################################


binary_num = input("Enter binary number >>> ")


def create_value_indexes():
    num_len = len(binary_num)
    value_index = []
    binary_num_index = []
    index_value = 1

    # creates arrays storing the binary number, and one storing the binary value index
    for i in range(0, num_len, 1):
        if int(binary_num[i]) == 0 or int(binary_num[i]) == 1:
            binary_num_index.append(binary_num[i])  # stores num index
            value_index.insert(0, index_value)  # stores value index
            index_value = index_value * 2
        else:
            exit("[-] Please enter only 1's and 0's ")
    return binary_num_index, value_index


def decode_values(num_index, value_index):
    # if num_index of i = 1, then value = value = value_index of i
    # value_index =[8, 4, 2, 1]
    # num_index =  [1, 0, 1, 0]
    # decode_index=[8, 0, 2, 0]
    # total = 8 + 0 + 2 + 0
    # total = 10

    # converts binary number into base 10 values
    decoded_index = []
    for i in range(0, len(num_index), 1):
        if int(num_index[i]) == 1:
            value = value_index[i]
            decoded_index.append(value)
        else:
            value = 0
            decoded_index.append(value)

    # prints total
    total = 0
    for j in range(0, len(decoded_index), 1):
        total = total + decoded_index[j]
    print("[+] Decoded number = " + str(total))


# binary_num_index contains (i.e) [1, 0, 1, 1]. value index contains (i.e) [32, 16, 8, 4, 2, 1]
(binary_num_index, value_index) = create_value_indexes()
decode_values(binary_num_index, value_index)

