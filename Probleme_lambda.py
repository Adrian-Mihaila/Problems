# P1, filter even and uneven ints from a list
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x: x % 2 == 0, lst))
uneven = list(filter(lambda x: x % 2 != 0, lst))
print(even)
print(uneven)

# P2, return square and cubic. Filter filters and map transforms
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sq = list(map(lambda x: x ** 2, lst))
cube = list(map(lambda x: x ** 3, lst))
print(sq)
print(cube)

# P3
found = lambda x: x.startswith('P')
print(found("Python"))

# P4. Return each word that starts with "e" from a string
# rez 1
s = " test jakld aksjdoi eue djcne nejd"
for _ in s.split():
    if _[0] == "e":
        word = _
        print(word)
# rez 2 cu lambda
s = " test jakld aksjdoi eue djcne nejd"
word = list(filter(lambda x: x[0] == "e", s.split()))
print(word)

# P5 common elements in 2 lists
a1 = [1, 2, 3, 5, 7, 8, 9, 10]
a2 = [1, 2, 4, 8, 9]
intersection = sorted(set(a1) & set(a2))
intersection_lambda = list(filter(lambda x: x in a1, a2))
print(intersection)

# P6. rearrange the list, sort it and leave the negative at the end
ls = [-1, 2, -3, 5, 7, 8, 9, -10]
negative = sorted(filter(lambda x: x < 0, ls))
positive = sorted(filter(lambda x: x > 0, ls))
result = positive + negative
print(result)

# P7 add two lists
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
result = list(map(lambda x, y: x + y, nums1, nums2))
print(result)

# P8 return the student with second lowest grade
students = [['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]
func = list(sorted(students, key=lambda x: x[1]))  # sort by grade
result = [func[i][0] for i in range(len(func)) if func[i][1] > func[0][1]][0]
print(result)

# P9 return palindromes
ls = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
palindromes = list(filter(lambda x: x == x[::-1], ls))
print(palindromes)

# P10 anagrams
# Without lambda
ls = ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
anagrams = [i for i in ls if "abcd" == "".join(sorted(i))]
print(anagrams)
# With lambda. Counter() is returning a dict with the letters counted
from collections import Counter
ls = ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
result = list(filter(lambda x: (Counter("abcd") == Counter(x)), ls))
print(result)

 

