#!/usr/bin/python

#Initialize a function

#Global Variable
myList=[29,39]

def function_name(myList):
	"The changes a passed list into this function..."
	#Local Variable
	#myList=[1,2,3]
	myList.append([10,20,30])
	print('Values inside the function is:', myList)
	return


#Calling the function
#Global Variable
#myList=[33,44,555]
function_name(myList)
print("Values outsied the function:", myList)
