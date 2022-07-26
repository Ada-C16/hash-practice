
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """
    pass
# empty hashtable (dict)
empty = {}
# key is the tuple of letters and the value = are all the words that have some combo of those letters in the tuple
# loop the list of strings (each word) 
for word in strings:
    new_tuple = []
# loop through each word in the list of strings
    for letter in word:
        new_tuple.append(letter)
# the order you put things in list, is the order they're appear in a tuple
#how are you gonna tell if the tuple of eat or tea?
#use built in methods, to sort it out- to ensure tuples appear in same order before you put in dict
pass 

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

