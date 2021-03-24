/*
My first c++ program:
The good old binary decoder.

Written by JamminCoder
3/24/2021
*/


#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Returns the base10 values needed to decode
// the binary number
vector<int> get_values(string binary_string)
{
	int n = 1;
    
    // Initialize vector
	int length = binary_string.size();
	int last_index = length - 1;
	vector<int> values(length, 0);
    
	for(int i = 0; i < length; i++)
	{
            // Adds the value of n to the last index.
            // The value of the last index decreases each loop
            // so that the value of n is added to indices in desending order.
            // If the binary number's length is 4, then the values vector will look like:
            // [8, 4, 2, 1]
			values[last_index] = n;
			n *= 2;
			last_index--;
	}
	return values;
}

// Decodes binary number to base10
int decode(string binary_string, vector<int> bin_values)
{
	int result = 0;
	for(int i = 0; i < binary_string.size(); i++)
	{
        // If the current index's value is 1, add the
        // corresponding value of bin_value to result
        // If anything other than a 1 or a 0 is entered,
        // then that value is treated as a 0.
		if(binary_string[i] == '1')
		{
			result += bin_values[i];
		}
	}
	return result;
}

int main()
{
	cout << "Enter binary number >> "; 
	string binary_string;
	getline(cin, binary_string); // Get the binary number
	vector<int> values = get_values(binary_string); // Get the base10 values needed to decode it
	int base_10_num = decode(binary_string, values); // Returns the base10 number
	cout << ">>> Decoded to " << base_10_num << endl;
}