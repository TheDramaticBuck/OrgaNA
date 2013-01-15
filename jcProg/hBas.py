# This file contains all the standard HTML stuff that
# needs to be used in the page.


# html large structure
def htmlStart():
	print("<!DOCTYPE html>\n<html>\n<head>")

def bodyStart():
	print('</head>\n<body>\n<div id="outWrapper">\n<div id="inWrapper">')

def htmlEnd():
	print("</div>\n</div></body>\n</html>")

# # # # # # # # # # # # # #
# # # Header Contents # # # 
# # # # # # # # # # # # # #

def htmlTitle(x):
	zipName=x
	print("<title> %s </title>" % zipName)

# The css file
def htmlCSS(x):
	cssPath=x
	print('<link rel="stylesheet" type="text/css" href="%s"/>' % cssPath)

# The global jquery file
def htmlJQ():
	print('<script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js"></script>\n')

# the local jscript file
def htmlLJS(x):
	jsPath=x
	print('<script language="javascript" src="%s" type="text/javascript"></script>\n' % jsPath)


# # # # # # # # # # # # #
# # # Body Contents # # #
# # # # # # # # # # # # #

# # Top Bar
def htmlStartTB():
	print('<div id="topBar">')

def htmlEndTB():
	print('</div>')

# # Top bar results Display
# # # #

def html_sysStats():
	outPut="""
	<table>
	<tr><td>Files:</td><td>%d</td></tr>
	<tr><td>Users:</td><td>%d</td></tr>
	<tr><td>Entries:</td><td>%d</td></tr>
	<tr><td></td><td></td></tr>
	</table>
	"""
	return outPut


# left Column
def htmlStartLC():
	print('<div id="leftColumn">')

def htmlEndLC():
	print('</div>')

# right Column
def htmlStartRC():
	print('<div id="rightColumn">')

def htmlEndRC():
	print('</div>')

def htmlClearDiv():
	print('<div class="clearBoth"></div>')

