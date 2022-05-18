import collections

# def grouped_anagrams(strings):
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: ?
        Space Complexity: ?
    """
    # Time Complexity: O(nmlog(m)) where n is the length of the strings and m is the length of  the character in the string
    # Space Complexity: O(n)
    if strings == []:
        return []
    grouped_anagram_list = []
    sorted_strings =[''.join(sorted(string)) for string in strings]
    dic = {}
    for i, word in enumerate(sorted_strings):
        dic.setdefault(word,[]).append(i)
    for value in dic.values():
        words = [strings[i] for i in value]
        grouped_anagram_list.append(words)
    return grouped_anagram_list
        

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: ?
        Space Complexity: ?
    """
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    key_dic = {}
    value_dic = {}
    for num in nums:
        if num in key_dic:
            key_dic[num] += 1
        else:
            key_dic[num] = 1
    for key, value in key_dic.items():
        if value in value_dic:
            value_dic[value].append(key)
        else:
            value_dic[value] = [key]
    output = []
    for i in range(len(nums),0,-1):
        if i in value_dic:
            output.extend(value_dic[i])
        if len(output) == k:
            break
    return output


def valid_sudoku(table):
    """ This method will return true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: ?
        Space Complexity: ?
    """
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    cols = collections.defaultdict(list)
    rows = collections.defaultdict(list)
    squares = collections.defaultdict(list)
    
    for r in range(9):
        for c in range(9):
            if table[r][c] == '.':
                continue
            if (table[r][c] in rows[r] or 
                table[r][c] in cols[c] or 
                table[r][c] in squares[r//3,  c//3]):
                return False
            cols[c].append(table[r][c])
            rows[r].append(table[r][c])
            squares[r//3, c//3].append(table[r][c])
    return True

