
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

def printFileData(fileList):
	counter=1
	for eachItem in fileList:
		print('<div id="fileDiv%d" class="theFiles">'% counter)
		print(eachItem)
		print('</div>')
		counter+=1
