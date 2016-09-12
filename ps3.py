###### this is the third .py file ###########

print "1. Add new record"
print "2. Delete record"
print "3. modify record"
print "4. show record "
print "5. Exit "
dict={}
d=dict

while true:
  print "enter value of choice"
  choice=int(input())

	if (choice==1):
		print "enter name"
		name=str(input());
		d.setdefault(name, [])
		print "City: ",
		city=input();
		print "District:",
		dist=input()
		print "State : ",
		state=input();
		d[name].append(city)
		d[name].append(dist)
		d[name].append(state)
		
        if (choice==2):
		name=input();
		for name in d:
			del d[name]
                continue

	if (choice==3):
		name=input().strip();
		for name in d:
			del d[name]
		d.setdefault(name, [])
		print "City: ",
		city=input();
		print "District:",
		dist=input()
		print "State : ",
		state=input();
		d[name].append(city)
		d[name].append(dist)
		d[name].append(state)
		continue
	if (choice==4):
		name=input();
		print d[name]
		continue
		
	if (choice==5):
		break

print "enter name"
name=input();
b=list();
for name in d:
	l=d[name]
	for var in l:
		var=var[0:3]
		b.append(var.upper())		
		
	print "H_CC_NO = " , b

