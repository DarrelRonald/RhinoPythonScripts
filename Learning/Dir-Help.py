"""
These are some samples of using the dir() and help() builtin functions from Python.
They are good for looking up helpful information within your IDE. 
As an alternative, you can just look at the full API documentation or the python scripts themselves.
"""
# Samples of dir() and help() with .NET modules
import System
print dir(System.Collections)
help(System.Collections.ArrayList)

import sys
print dir(sys)
help(sys)


#---- Samples of dir() and help() with Rhino specific Python modules
import rhinoscriptsyntax as rs
print dir(rs)
help(rs.Command)

import scriptcontext as sc
print dir(sc)
help(sc.doc)

import Rhino as rh
print dir(rh)
print dir(rh.DocObjects)
print dir(rh.DocObjects.Tables)
print dir(rh.DocObjects.Tables.ObjectTable)
help(rh.DocObjects.Tables.ObjectTable.Delete)