import math
import os
import random
import re
import sys

"""
Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. 
Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

Example:
s = mom
The list of all anagrammatic pairs is [m, m], [mo, om] at positions [[0], [2]], [[0, 1], [1, 2]] respectively.

Function Description:
Complete the function sherlockAndAnagrams in the editor below.

sherlockAndAnagrams has the following parameter(s):

    string s: a string

Returns

    int: the number of unordered anagrammatic pairs of substrings in s

Input Format

The first line contains an integer q, the number of queries.
Each of the next q lines contains a string s to analyze. 

Complete the 'sherlockAndAnagrams' function below.

The function is expected to return an INTEGER.
The function accepts STRING s as parameter.
"""

def sherlockAndAnagrams(s):
    # dictionary where all the substrings of s and the amount of times they appear are stored
    substring_counter = {}
    
    # will traverse the string and store every possible substring (sorted) in the substring_couner dictionary
    for i in range(1, len(s)):
        for j in range(0, len(s)-i+1):
            if (substring_counter.get("".join(sorted(s[j:j+i]))) != None):
                if (substring_counter["".join(sorted(s[j:j+i]))] > 0):
                    substring_counter["".join(sorted(s[j:j+i]))] += 1
            else:
                substring_counter["".join(sorted(s[j:j+i]))] = 1
    
    # will now count all of the sorted substrings that appear more than once to see how many anagrams there are
    total = 0
    for i in substring_counter.values():
        if i > 1:
            total += (i * (i - 1)) // 2
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
