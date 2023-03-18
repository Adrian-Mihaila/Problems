# Scramblies. Return true if s2 is in s1 or false if not.

# # Rezolvare 1 O(n*m)
def scramble(s1, s2):
    s1 =list(s1)
    s2 =list(s2)
    
    for _ in s2:
        if _ in s1:
            s1.remove(_)
        else:
            return False
    return True

print(scramble('cedewaraaossoqqyt', 'codewars'))

# # Rezolvare 2 O(n)
def scramble(s1, s2):
    freq = {}
    
    for c in s1:
        freq[c] = freq.get(c, 0) + 1
        # if not freq.get(c):
        #     freq[c] = 0
        # freq[c] +=1

    for c in s2:
        if c not in freq or freq[c] <= 0:
            return False
        freq[c] -= 1
        
    return True
    
print(scramble('cedewaraaossoqqyt', 'codewars'))

# Rezolvare 3
def scramble(s1,s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True

# Rezolvare 4
from collections import Counter
def scramble(s1,s2):
    # Counter basically creates a dictionary of counts and letters
    # Using set subtraction, we know that if anything is left over,
    # something exists in s2 that doesn't exist in s1
    return len(Counter(s2)- Counter(s1)) == 0

# Rezolvare 5
def scramble(s1, s2):
    return not any(s1.count(char) < s2.count(char) for char in set(s2))

# Rezolvare 6
def scramble(s1,s2):
    return all( s1.count(x) >= s2.count(x) for x in set(s2))

# Rezolvare 7
from collections import Counter
def scramble(s1, s2):
    # Python 3.10 rich comparison operators for Counter ftw!
    return Counter(s2) <= Counter(s1)

# Rezolvare 8
scramble=lambda a,b,c=__import__('collections').Counter:not c(b)-c(a)

# Rezolvare 9
from collections import Counter
def scramble(s1,s2): return len(Counter(s2) - Counter(s1)) == 0
