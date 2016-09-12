###### this is the first .py file ###########import sys
import sys
import collections
print sys.argv[1:]
dict = {}
for word in sys.argv[1:]:
	if word not in dict.keys():
  		dict[word] = 1
 	else:
  		dict[word] += 1

print dict

# Function to find top 3 words
def top3words(dict):
	counts = collections.Counter(dict)
	return [elem for elem, _ in counts.most_common(3)]
#function calling
top = top3words(dict)
print top

####### write your code here ##########
