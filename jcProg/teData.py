
def getUserList(x):
	theData=x
	usrList=theData.split('\n')
	usrSet=set()
	for eachItem in usrList:
		usrSet.add(eachItem)
	return usrSet

class getFileData:
	def __init__(self,fileData):
		self.fileData=fileData
		self.postList=fileData.split('n')

	def userNumb(self):
		userSet=set()
		for eachItem in self.postList:
			userSet.add(eachItem)
		return len(userSet)
	
	def contNumb(self):
		userList=self.postList
		return len(userList)
		
