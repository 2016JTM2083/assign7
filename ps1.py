###### this is the first .py file ###########
              
import sys              			#Import sys to get command line arguements
import collections      			#Import collections

print sys.argv[1:]
dict = {}
for word in sys.argv[1:]:
	if word not in dict.keys():
  		dict[word] = 1
 	else:
  		dict[word] += 1

print dict

	
def top3words(dict):				# Function to find top 3 words
	counts = collections.Counter(dict)
	return [elem for elem, _ in counts.most_common(3)]



top = top3words(dict)				#function calling
print top


