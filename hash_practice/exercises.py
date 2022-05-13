#time O(m * nlogn)
#space O(n)

def grouped_anagrams(strings):
    anagrams = {}
    for word in strings:
        sortedWord = "".join(sorted(word))
        if sortedWord in anagrams:
                anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]
    return list(anagrams.values())

#time O(1)
#space O(n)
def top_k_frequent_elements(nums, k):
    if len(nums) == 0:
        return []
    else:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        result = []
        
        for number in nums:
            count[number]=count.get(number,0)+1
        for number, count in count.items():
            freq[count].append(number)
        
        for i in range(len(freq)-1,0,-1):
            for number in freq[i]:
                result.append(number)
                if len(result)==k:
                    return result

#time O(1)
#space O(1)
def valid_sudoku(table):
    rows = {r: set() for r in range(9)}
    col = set()
    box_grid_1 = set()
    box_grid_2 = set()
    box_grid_3 = set()

    row_count = 1
    for r in range(9):
        for c in range(9):
            if table[r][c] == ".": continue
            if table[r][c] in rows[c] or table[r][c] in col:
                return False
            rows[c].add(table[r][c])
            col.add(table[r][c])
            if c < 3:
                if table[r][c] in box_grid_1: return False
                else: box_grid_1.add(table[r][c])
            elif c < 6: 
                if table[r][c] in box_grid_2: return False
                else: box_grid_2.add(table[r][c])
            else:
                if table[r][c] in box_grid_3: return False
                else: box_grid_3.add(table[r][c])
        if row_count%3 == 0:
            box_grid_1, box_grid_2, box_grid_3 = set(), set(), set()
        col = set()
        row_count += 1

    return True

