"""
Inputs:
   none
Outputs:
   AllModules: List of all modules from all sys.path
   AllPaths: List of all sys.path locations set within Rhino and Grasshopper
   LimitedPathModules: List of all modules within the one path selected
"""

__author__ = "Darrel Ronald"
__copyright__ = "Copyright 2020"
__credits__ = "[Anders Deleuran, Darrel Ronald]"
__license__ = "MIT License"
__version__ = "0.0.1"
__maintainer__ = "Darrel Ronald"
__email__ = "darrel@spatiomatics.com"
__status__ = "Development"

import sys
import os

allPaths = []
allModules = []
oneModule = []

# Get all sys.path locations
for p in sys.path:
    allPaths.append(p)
print allPaths


def getIronPythonModules():
    """ Traverse path directories and get names of files/sub-directories """
    for p in sys.path:
        for n in os.listdir(p):
            allModules.append(n)

def getLimitedIronPythonModules(int):
    """ Traverse specific path directory and get names of files/sub-directories """
    for n in os.listdir(allPaths[PathIndex]):
        oneModule.append(n)

getIronPythonModules()
getLimitedIronPythonModules(PathIndex)

AllModules = allModules
AllPaths = allPaths
LimitedPathModules = oneModule


#-----------------------------------
# Test of IronPython imports
# Based on: https://ironpython-test.readthedocs.io/en/latest/howto/urllib2.html

import urllib2
response = urllib2.urlopen('http://www.maketank.org/')
html = response.read()
#print html
#print dir(urllib2)

import json
#print dir(json)