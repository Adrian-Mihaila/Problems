# Scramblies. Return true if s2 is in s1 or false if not.

# O(n*m)
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

# O(n)
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
