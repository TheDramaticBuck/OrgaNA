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

# # # # # # # # # # # # # # # # # # # #
# # # # # # ZIP FILE STUFF  # # # # # #
# this reads the zipFile

readZip=zipfile.ZipFile("dwn/Threads.zip","r")

# This ceates a list of all the files in the zipfile
fileList=readZip.namelist()

# starts the zip file as an object
theZipF=sysData.systemData(readZip)

# the title of the page by taking the name
# of the zip file
zipName="Forum"

# # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # #  Start the HTML structure # # # # # #

# # # # # START HEADER SECTION # # # # # #
hBas.htmlStart()                         #

# Sets the page title
theTitle=("%s System Stats" % zipName)
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


## ## ## ## ## ## ## ## ## ## ## ##
## ## ## START TOP STAT BAR## ## ##
hBas.htmlStartTB()				 ##

print('<h1>%s System Stats</h1>'%zipName)



hBas.htmlEndTB()				 ##
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
hBas.htmlStartRC()               ##

print('<h1>Items in Right Column</h1>')

t_files=theZipF.totalFiles()
t_users=theZipF.totalUsers()
t_posts=theZipF.totalPosts()

t_coreUsers=theZipF.totalCoreUsers()

print(t_coreUsers)

# Loads the html formating to a variable
html_sysStats=hBas.html_sysStats()

# Prints all the results on the top bar with
# formating from the hBas file.
print(html_sysStats % (t_files,t_users,t_posts))


hBas.htmlEndRC()                 ##
## ## ## END RIGHT COLUMN  ## ## ##
## ## ## ## ## ## ## ## ## ## ## ##

hBas.htmlClearDiv()

# end the html
hBas.htmlEnd()
