# s = "Saransh"

# # Q1 find total occurance of a 
# print("Total Occurance of a is : ",s.count("a"))

# # Q2 Find 1st occurance of n
# print("First Occurance of n in index : ", s.find("n"))

# # Q3 Use swapcase for changing the current case of string
# print(s.swapcase())

# # Q4 Split and join 
# s1 = "saransh,age,ysm"
# s1 = s1.split(",")
# s1 = "|".join(s1)
# print(s1)

# # Q5 Partition
# spd = "saransh-prasad-bari"
# print(spd.partition("-"))
# print(spd.rpartition("-"))

# # Q6 Translate
# table = str.maketrans("aeiou-", "***** ")
# trans = spd.translate(table)
# print(trans)


# Q7  Find the first non repeating character in string 
from collections import Counter
# counter class counts the number of occurence of each character 
# s = "saransh" -> Counter({'s': 2, 'a': 2, 'r': 1, 'n': 1, 'h': 1})
def firstNonRepeating(s):
    count = Counter(s)
    for idx, char in enumerate(s):
        if count[char] == 1:
            return idx
    return -1
print(firstNonRepeating("saransh"))

# Q8 Find the maximum length of substring where all characters are unique.
s = "saransh"
def ls(s):
    seen = set() 
    left = 0
    max_len = 0
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len

print(ls(s))

# Q9 Find rotation of string 
s1,s2 = "abcd", "bcad"
def isRotation(s1,s2):
    if len(s1) != len(s2):
        return False
    return s2 in (s1+s1)
print(isRotation(s1,s2))

