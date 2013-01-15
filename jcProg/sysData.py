import teData

### ### Items in the left Column ### ###

# Creates DropDown file menu
def dropDownMenu(x):
	from re import sub
	theList=x
	print('<div id="fileSelect">\nSelect File')
	print('<select id="zipFiles">')
	counter=1
	for eachItem in theList:
		fileName=sub(".txt","",eachItem)
		print('<option value="fileDiv%d"> %s </option>' % (counter,fileName))
		counter+=1
	print('</select>\n</div>')

# Table of stats for each team
def printFileData(readZip):
	theZip=readZip
	fileList=theZip.namelist()
	counter=1
	for eachItem in fileList:
		fileData=readZip.read(eachItem)
		fileCont=teData.getFileData(fileData)
		usN=fileCont.userNumb()
		usC=fileCont.contNumb()
		conMean='{:.3f}'.format(usN/float(usC))
		print('<div id="fileDiv%d" class="theFiles">'% counter)
		print("<h3> %s </h3>" % eachItem)
		print('<table>')
		print('<tr>')
		print('<td>Number of Users</td><td>%i</td>' % usN)
		print('</tr>\n<tr>')
		print('<td>Number of Contributions</td><td>%i</td>' % usC)
		print('</tr>\n<tr>')
		print('<td>Mean Contributions</td><td>%s</td>' % conMean)
		print('</tr>')
		print('</table>')
		# print(fileData)
		print('</div>')
		counter+=1

# Items in the top info Bar
# A class that will read each file in the zip
# and get the data of all the users
class systemData():
	
	def __init__(self,readZip):
		self.readZip=readZip
		self.fileList=readZip.namelist()

	def totalUsers(self):
		userSet=set()
		for eachItem in self.fileList:
			fileData=self.readZip.read(eachItem)
			users=fileData.split('\n')
			for eachUser in users:
				userSet.add(eachUser)
		return(len(userSet))

	def totalPosts(self):
		totalPosts=[]
		for eachItem in self.fileList:
			fileData=self.readZip.read(eachItem)
			users=fileData.split('\n')
			for eachUser in users:
				totalPosts.append(eachUser)
		return(len(totalPosts))

	def totalFiles(self):
		return len(self.fileList)
	
	def totalCoreUsers(self):
		# this will need to call a more
		# complicated script from get layers
		import getLayers
		# it will start by just reading the zipfile
		# and then letting the other thing do the rest
		sysLayers=getLayers.netLayers(self.readZip)
		what=sysLayers.userStatDF()
		return what
