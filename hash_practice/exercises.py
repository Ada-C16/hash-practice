
from array import array
from distutils.log import error
import string


def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """
    
    words = [strings]  #this is an array with strings in it 
    for strings in words: 
        if sorted(words[0]) == sorted(words[1]):
            sorted(words[0]) = []
            if(sorted(strings)== sorted(strings)):   
        print(string) 

#expected_answer = [
        ["ate","eat","tea"],
        ["nat","tan"],
        ["bat"]
   #   ]

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """
    pass


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: ?
        Space Complexity: ?
    """
    pass

