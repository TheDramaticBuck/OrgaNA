#!/opt/local/bin/python

# from jcProg import hBas
from jcProg import sysData,hBas,teData,copData
import zipfile

# for debugging
import cgitb
cgitb.enable()

print("Content-Type: text/html\n")

# # # # # # # # # # # # # # # # # # # #
# # # # # # ZIP FILE STUFF  # # # # # #
# this reads the zipFile

readZip=zipfile.ZipFile("dwn/Threads.zip","r")

# This ceates a list of all the files in the zipfile
fileList=readZip.namelist()


# the title of the page by taking the name
# of the zip file
zipName="Forum"

# A good idea to start some global variables....

## Global file list
zipFileList=readZip.namelist()

## Global full user list
t_fullEntries=copData.getFullEntries(readZip)

## Global user set
t_userSet=set(t_fullEntries)


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


t_files=len(zipFileList)
t_users=len(t_userSet)
t_posts=len(t_fullEntries)

# Loads the html formating to a variable
html_sysStats=hBas.html_sysStats()

# Prints all the results on the top bar with
# formating from the hBas file.
print(html_sysStats % (t_files,t_users,t_posts))

c_Stats=copData.copStats(t_fullEntries)
print(len(c_Stats.userSet))
print(len(c_Stats.rawUserList))

print(c_Stats.getUsersInLayer(2))

hBas.htmlEndRC()                 ##
## ## ## END RIGHT COLUMN  ## ## ##
## ## ## ## ## ## ## ## ## ## ## ##

hBas.htmlClearDiv()

# end the html
hBas.htmlEnd()
