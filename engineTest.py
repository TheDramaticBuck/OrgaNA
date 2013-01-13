#!/opt/local/bin/python

# This is for debugging, always have it
# to make sure we know where the errors come from.
import cgi
import cgitb
cgitb.enable()


print("Content-Type: text/html\n")

list1=[1,2,3,4,5]

# This is 100% where I need a class.
def getComs(list):
	counter=0
	for i in range(0,len(list)):
		for j in range(i+1,len(list)):
			print(list[i])
			print(list[j])
			print("<br>")
			counter+=1
	print("%d Combinations" % counter)

# getComs(list1)

# # # The above worked, but now for something more complicated # # #
# # # # # # The freaking class! # # # # # # 
# the object for this thing will have to be the file that I am reading
# there are also a number of things that will have to be taken into account, such 
# as the length of the list, the combinations and all the other stuff.


class fileList:
	"This will give all the list info"
	def __init__(self,theList):
		self.theList=theList
	
	def allCombs(self,x):
		comLen=0
		for i in range(0,len(self.theList)):
			for j in range(i+1,len(self.theList)):
				vOne=list1[i]
				vTwo=list1[j]
				comLen+=1
				if x=="lis":
					print("%d and %d<br>" % (vOne,vTwo))
		if x=="len":
			print(comLen)

	def listLength(self):
		print(len(self.theList))
		print("<br>")

mine=fileList(list1)

mine.listLength()

mine.allCombs("lis")
