#!/opt/local/bin/python

# from jcProg import hBas
from jcProg import sysData,hBas,teData
import zipfile

# for debugging
import cgitb
cgitb.enable()

# project path
#import os
#gettext = lambda s: s
#PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

print("Content-Type: text/html\n")

# this reads the zipFile
readZip=zipfile.ZipFile("dwn/Threads.zip","r")

# This ceates a list of all the files in the zipfile
fileList=readZip.namelist()

# the title of the page by taking the name
# of the zip file
zipName="Archive"
theTitle=("%s System Stats" % zipName)

# Start the HTML structure

# # # # # START HEADER SECTION # # # # # #
hBas.htmlStart()
hBas.htmlTitle(theTitle)

# add the css page
hBas.htmlCSS("main.css")

# add jQery library
hBas.htmlJQ()

# add local jscript
hBas.htmlLJS("main.js")

# # End the header
hBas.bodyStart()

# # # # # START MAIN BODY # # # # # #

print("<h1> %s System Stats</h1>" % zipName)

## ## ## ## ## ## ## ## ## ## ## ##
## ## ## START TOP STAT BAR## ## ##
                                 ##
hBas.htmlStartTB()

# the number of files (networks)
noFiles=len(fileList)
print("%d groups in total<br>" % noFiles)

hBas.htmlEndTB()
                                 ##
## ## ## END TOP STAT BAR  ## ## ##
## ## ## ## ## ## ## ## ## ## ## ##


## ## ## ## ## ## ## ## ## ## ## ##
## ##  START THE LEFT COLUMN  ## ##
                                 ##

# dropdown menu for each file
hBas.htmlStartLC()

sysData.dropDownMenu(fileList)
sysData.printFileData(readZip)

hBas.htmlEndLC()

                                 ##
## ## ##  END LEFT COLUMN  ## ## ##
## ## ## ## ## ## ## ## ## ## ## ##


## ## ## ## ## ## ## ## ## ## ## ##
## ## START THE RIGHT COLUMN  ## ##
                                 ##

hBas.htmlStartRC()
print('<h1>Items in Right Column</h1>')
hBas.htmlEndRC()

                                 ##
## ## ## END RIGHT COLUMN  ## ## ##
## ## ## ## ## ## ## ## ## ## ## ##

hBas.htmlClearDiv()

# end the html
hBas.htmlEnd()
