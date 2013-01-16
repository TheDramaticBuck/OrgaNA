
from numpy import *
from pandas import *

# get the full list of users
def getFullEntries(readZip):
	fullUserList=[]
	fileList=readZip.namelist()
	for eachFile in fileList:
		fileData=readZip.read(eachFile)
		users=fileData.split("\n")
		for eachEntry in users:
			fullUserList.append(eachEntry)
	return fullUserList

# All data including layers
class copStats():
	def __init__(self,entryList):
		self.rawUserList=entryList
		self.userSet=set(entryList)

	def userDF(self):
		sDF=DataFrame(self.rawUserList)

		# get post frequency
		postFreq=sDF[0].value_counts()
		totalPosts=sum(postFreq)

		# post percentage
		userPC=postFreq/float(totalPosts)

		# cumulative percentages
		cumPC=cumsum(userPC)

		# construct dataframe
		fullDF=DataFrame({
			"Frequency":postFreq,
			"Percentage":userPC,
			"Cummulative":cumPC,
		})
		
		# add layers
		fullDF["Layer"]=where(fullDF["Cummulative"]<0.33,1,fullDF["Cummulative"])
		fullDF["Layer"]=where(fullDF["Cummulative"]>0.33,2,fullDF["Layer"])
		fullDF["Layer"]=where(fullDF["Cummulative"]>0.66,3,fullDF["Layer"])

		return fullDF["Layer"]

	def getUsersInLayer(self,x):
		if x==1 or x=="1":
			return "Layer 1 was called for"

		elif x==2 or x=="2":
			return "Layer 2 was called for"

		elif x==3 or x=="3":
			return "Layer 3 was called for"
