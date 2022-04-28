def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(n * n * nlogn ) = O(n^3 log n) oops
        Space Complexity: # O(n)
    """
    anagrams = {}
    for s in strings:
        alphabetized_s = ''.join(sorted(s)) # n * n log n
        if alphabetized_s in anagrams:
            anagrams[alphabetized_s].append(s)
        else:
            anagrams[alphabetized_s] = [s]
    return [anagram_list for anagram_list in anagrams.values()]

    # party in the graveyard
    #
    # ({str: matches})
    # { map_id: list of matches}

    # fmaps = ({"default": 1})
    # matches = {}

    # for s in strings:
    #     s_map = freq_map(s)
    #     if s_map in fmaps:
    #         matches[id(s_map)].append(s)
    #     else:
    #         fmaps.add(s_map)
    #         matches[id(s_map)] = [s]

    # return [anagram_list for anagram_list in matches.values()]


def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n*m) -> O(n^2) (could maybe reduce by removing keys in dict as used)
        Space Complexity: O(2n) -> O(n)
    """
    fmap = {} #TC: O(n) SC: O(n)
    for x in nums:
        if x in fmap:
            fmap[x] += 1
        else:
            fmap[x] = 1
    decreasing_freq_order = [] # SC: O(n)
    for x in range(len(nums), 0, -1): #O(n)
        for e, freq in fmap.items(): #O(m) # use that python dict is in order of first appearance
            if freq == x:
                decreasing_freq_order.append(e)
                # fmap.pop(e)
    return decreasing_freq_order[:k]

def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(n^2)
        Space Complexity: O(n)
    """
    # row-wise
    for row in table: # O(9)
        freq_row = {}
        for e in row: # O(9)
            if freq_row.get(e) and e != ".":
                return False
            else:
                freq_row[e] = True

    # column-wise # O(9*9) or more generally O(n*n)
    for col in range(len(table[0])): # O(9) but generalized
        freq_col = {}
        for row in table:
            if freq_col.get(row[col]) and row[col] != '.':
                return False
            else:
                freq_col[row[col]] = True

    # box-wise # O(3*3*n*n)
    for rows in range(3):
        for cols in range(3):
            box = {}
            for x in table[rows*3: (rows+1)*3]:
                for y in x[cols*3: (cols+1)*3]:
                    if box.get(y) and y != '.':
                        return False
                    else:
                        box[y] = True
    return True