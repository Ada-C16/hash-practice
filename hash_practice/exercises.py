
def grouped_anagrams(strings):
    """ This method will return an array of arrays.
        Each subarray will have strings which are anagrams of each other
        Time Complexity: O(m * nlogn) where m is the length of strings and n is the length of the longest string in strings
        Space Complexity: O(n)
    """
    sorted_strings = {}
    output = []

    for s in strings:
        s_list = list(s)
        s_list.sort()
        sorted_s = "".join(s_list)
        if sorted_s in sorted_strings:
            index = sorted_strings[sorted_s]
            output[index].append(s)
        else:
            sorted_strings[sorted_s] = len(output)
            output.append([s])

    return output

def top_k_frequent_elements(nums, k):
    """ This method will return the k most common elements
        In the case of a tie it will select the first occuring element.
        Time Complexity: O(n log(n))
        Space Complexity: O(n)
    """
    if not nums:
        return []
    
    freq_dict = {}

    for n in nums:
        if n in freq_dict:
            freq_dict[n] += 1
        else:
            freq_dict[n] = 1

    l = []
    
    for key, val in freq_dict.items():
        l.append({'number': key, 'freq': val})
    l.sort(key=sort_by_freq, reverse=True)

    most_freq = []

    for i in range(k):
        most_freq.append(l[i]['number'])

    return most_freq

def sort_by_freq(dict):
    return dict['freq']


def valid_sudoku(table):
    """ This method will return the true if the table is still
        a valid sudoku table.
        Each element can either be a ".", or a digit 1-9
        The same digit cannot appear twice or more in the same 
        row, column or 3x3 subgrid
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    columns = {
        0: set(), 
        1: set(), 
        2: set(),
        3: set(), 
        4: set(), 
        5: set(),
        6: set(), 
        7: set(),
        8: set(), 
}
    rows = {
        0: set(), 
        1: set(), 
        2: set(),
        3: set(), 
        4: set(), 
        5: set(),
        6: set(), 
        7: set(),
        8: set(), 
    }
    grids = {
        (0,0): set(),
        (0,3): set(),
        (0,6): set(),
        (3,0): set(),
        (3,3): set(),
        (3,6): set(),
        (6,0): set(),
        (6,3): set(),
        (6,6): set()
    }

    for row in range(len(table)):
        for col in range(len(table[0])):
            n = table[row][col]
            if n != ".":
                n = int(n)
                if n < 1 or n > 9:
                    return False
                if n in columns[col] or n in rows[row] or n in grids[(get_top_left(row), get_top_left(col))]:
                    return False
                else:
                    columns[col].add(n)
                    rows[row].add(n)
                    grids[(get_top_left(row), get_top_left(col))].add(n)

    return True

def get_top_left(row_or_col):
    return (row_or_col // 3) * 3