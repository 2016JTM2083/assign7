###### this is the second .py file ###########


import random,math						      #import packages for using random and maths functions
						       
no_users=input("Enter number of users \n") 		
count=0

								        #For loop to generate location of each user randomly
for i in range(no_users): 							 
	(x,y)=(random.random()*2- 1, random.random()*2-1)              
	dist=math.sqrt(x*x+y*y)    					# Find the distance of each user from origin
	if dist<=1:   							#Condition to check user lie within unit radius or not
		count+=1 

print "No. of users in unit radius:",count                 						
percentage=(float(count)/float(no_users))*100						
print "percentage of users in unit radius:",percentage

