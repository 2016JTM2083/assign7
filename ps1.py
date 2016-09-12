###### this is the first .py file ###########
import sys
wordstring=str(sys.argv)
wordlist = wordstring.split()
wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

print("String\n" + wordstring +"\n")
print("List\n" + str(wordlist) + "\n")
print("Frequencies\n" + str(wordfreq) + "\n")
print("Pairs\n" + str(zip(wordlist, wordfreq)))
####### write your code here ##########
