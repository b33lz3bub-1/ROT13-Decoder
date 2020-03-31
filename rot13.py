#!/usr/bin/env python3
import sys
l_upper = [ "A", "B", "C", "D", "E", "F",
        "G", "H", "I", "J", "K", "L",
        "M", "N", "O", "P", "Q", "R",
        "S", "T", "U", "V", "W", "X",
        "Y", "Z"]

l_lower = [ "a", "b", "c", "d", "e", "f",
            "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r",
            "s", "t", "u", "v", "w", "x",
            "y", "z"]
def rot13(word):
    plain = ""
    for s in range(len(word)):
        if word[s] not in l_upper and word[s] not in l_lower:
            plain += word[s]
        elif word[s] in l_upper:
            #print word[n]
            i = l_upper.index(word[s])
            k = ((i + 13) % 26)
            #print k
            #print l[k]:
            plain += l_upper[k]

        else:
            #print word[n]
            i = l_lower.index(word[s])
            k = ((i + 13) % 26)
            #print k
            #print l[k]
            plain += l_lower[k]
    plain += " "
    return plain
    #print plain 

string = sys.argv[1] 

#string = '''Jul qvq gur puvpxra pebff gur ebnq?'''
#string = string.upper()
s = string.split()
#print s
plain_text = ""
for i in s:
    plain_text += rot13(i)

print plain_text
    
