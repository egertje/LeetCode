import math
import os
import random
import re
import sys

"""
Ransom Note Challenge from HackerRank

Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him 
through his handwriting. He found a magazine and wants to know if he can cut out whole words from it and use 
them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must
use only whole words available in the magazine. He cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note 
exactly using whole words from the magazine; otherwise, print No.

Example
magazine = "attack at dawn"
note = "Attack at dawn"

The magazine has all the right words, but there is a case mismatch. The answer is No. 

Function Description

Complete the checkMagazine function in the editor below. It must print Yes if the note can be formed using the 
magazine, or No

checkMagazine has the following parameters:

    string magazine[m]: the words in the magazine
    string note[n]: the words in the ransom note

Prints

    string: either Yes or No, no return value is expected 

Complete the 'checkMagazine' function below.

The function accepts following parameters:
 1. STRING_ARRAY magazine
 2. STRING_ARRAY note
"""

def checkMagazine(magazine, note):
    # hash table that will store the number of occurrences of each word in the magazine
    m_hash_words = {}
    
    # find all the occurrences of all the words in the magazine and put it in the hash table
    for word in magazine:
        if (m_hash_words).get(word) != None:
            if (m_hash_words[word] > 0):
                m_hash_words[word] += 1
        else:
            m_hash_words[word] = 1
    
    # will check to make sure all words in the note are in the magazine
    for word in note:
        if (m_hash_words.get(word) is None or m_hash_words[word] == 0):
            return False
        else:
            m_hash_words[word] -= 1
    return True
        
            

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    answer = checkMagazine(magazine, note)
    
    if answer:
        print("Yes")
    else:
        print("No")
