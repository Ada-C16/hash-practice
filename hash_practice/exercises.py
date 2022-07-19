
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """
    anagrams={}
    anagram_list=[]
    for word in strings:
        sorted_word="".join(sorted(word))
        if anagrams.get(sorted_word):
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word]=[word]
    
    for word in anagrams.values():
        anagram_list.append(word)
    return anagram_list

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """
    freq_dict={}
    for num in nums:
        if num not in freq_dict:
            freq_dict[num]=1
        else:
            freq_dict[num]+=1
    sorted_dict=sorted(freq_dict.items(), key=lambda x:(x[1]), reverse=True)
    most_common =[]
    for elem in sorted_dict:
        most_common.append(elem[0])
    return most_common[:k]


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

