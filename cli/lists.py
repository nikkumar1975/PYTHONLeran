#lists in python
mylist=[]
mylist.append(2)
mylist.append(3)
mylist.append(5)
mylist.append(7)
i=0
for x in mylist:
	i=i+1
	print("mylist item# ", i, " :", x)	

print(mylist[0])
#print(mylist[10])	It will return error
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings = []
strings.append("hello")
strings.append("world")

names = ["John", "Eric", "Jessica"]


# write your code here
second_name = names[1]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)