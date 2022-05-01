
from tabnanny import check


def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n*m log m) 
        Space Complexity: O(n) since a hash table was created
    """
    group_anagrams = dict()
    for word in strings: #O(n) where n is the length of input
        sorted_ver = "".join(sorted(word)) #O(m log m) where m is the length of each word
        if sorted_ver not in group_anagrams:
            group_anagrams[sorted_ver] = [word]
        else:
            group_anagrams[sorted_ver].append(word)

    output = []
    for word_list in group_anagrams.values(): #O(n)
        output.append(word_list)
    return output
        

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(m*n)
        Space Complexity: O(n) for num_freq
    """
    if not nums:
        return nums

    num_freq = dict() #O(n) for space
    
    for num in nums: #O(n) for time
        if num not in num_freq:
            num_freq[num] = 1
        else:
            num_freq[num] += 1

    output = []
    for i in range(k): #O(m) for time
        if len(output) == k:
            return output
        max_value = max(num_freq.values())
        for key,val in list(num_freq.items()): #O(n) for time where n is the length of nums, also O(n) to cast into list
            if val == max_value:
                output.append(key)
                del num_freq[key]
    return output


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(n^2)
        Space Complexity: O(n) for all the sets created
        // Not sure about time and space complexity for this one!
    """
    if check_if_row_valid(table) and check_if_column_valid(table) and check_if_subgrid_valid(table):
        return True
    else:
        return False

def check_if_row_valid(table):
    unique = set() # O(n) for space
    for a in range(9): # O(n) for time
        for b in range(9): # O(n) for time
            if table[a][b] not in unique and table[a][b] != ".":
                unique.add(table[a][b])
            elif table[a][b] in unique and table[a][b] != ".":
                return False
        unique = set()
    return True

def check_if_column_valid(table):
    unique = set() # O(n) for space
    for a in range(9): # O(n) for time
        for b in range(9): # O(n) for time
            if table[b][a] not in unique and table[b][a] != ".":
                unique.add(table[b][a])
            elif table[b][a] in unique and table[b][a] != ".":
                return False
        unique = set()
    return True

def check_if_subgrid_valid(table):
    unique = set() # O(n) for space
    for i in range(0, 9, 3): 
        for j in range(0, 9, 3): 
            for k in range(i, i+3) : 
                for l in range(j, j+3): 
                    if table[k][l] not in unique and table[k][l] != ".":
                        unique.add(table[k][l])
                    elif table[k][l] in unique and table[k][l] != ".":
                        return False
            unique = set()

    return True