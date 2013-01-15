
from numpy import *
from pandas import *

# need to put everything into a frame or something.

class netLayers():

	def __init__(self,readZip):
		self.readZip=readZip
		self.fileList=readZip.namelist()

	def readAndMakeList(self):
		userList=[]
		for eachFile in self.fileList:
			fileData=self.readZip.read(eachFile)
			users=fileData.split('\n')
			for eachUser in users:
				userList.append(eachUser)
		return userList

	def userStatDF(self):
		fullUserList=self.readAndMakeList()
		userDF=DataFrame(fullUserList)
		
		# The user name becomes the index
		# therefore freq values are 0
		userDF=userDF[0].value_counts()
		totalPosts=sum(userDF)
		
		# percentage of posts
		userPC=userDF/float(totalPosts)

		# cumulative perentage
		cumPC=cumsum(userPC)
		
		# build complete userData frame
		theDataFrame=DataFrame({
			"Frequency":userDF,
			"Percent":userPC,
			"Cumulative":cumPC,
			})
		
		# Conditionals for layers
		theDataFrame["Layer"]=where(theDataFrame["Cumulative"]<0.33,1,theDataFrame["Cumulative"])
		theDataFrame["Layer"]=where(theDataFrame["Cumulative"]>0.33,2,theDataFrame["Layer"])
		theDataFrame["Layer"]=where(theDataFrame["Cumulative"]>0.66,3,theDataFrame["Layer"])

		return theDataFrame["Layer"]

	def maxUserFreq(self):
		theDF=DataFrame(self.userStatDF())
		# outPut=max(theDF[1])
		return theDF.columns

	def getCore(self):
		answer="This shit be real!"
		return answer
	
	def true(self):
		return self.getCore()
