# Author: Justin Huang
# GitHub username: huangjus
# Date: 5/2/23
# Description: takes a filename as input, reads the numbers from the file, computes their sum, and writes the sum to a
# new file called sum.txt.

def file_sum(filename):
    """
    Reads a list of numbers from a text file, sums them up, and writes the result to another file.
    """

    with open(filename, 'r') as infile:
        numbers = infile.readlines()

    total = sum(float(num) for num in numbers)

    with open('sum.txt', 'w') as outfile:
        outfile.write(str(total))
        