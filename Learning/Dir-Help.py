"""
These are some samples of using the dir() and help() builtin functions from Python.
They are good for looking up helpful information within your IDE. 
As an alternative, you can just look at the full API documentation or the python scripts themselves.
"""

__author__ = "Darrel Ronald"
__copyright__ = "Copyright 2020, Spatiomatics"
__credits__ = "Darrel Ronald"
__license__ = "MIT License"
__version__ = "0.0.1"
__maintainer__ = "Darrel Ronald"
__email__ = "darrel@spatiomatics.com"
__status__ = "Developement"


#----Samples of dir() and help() with .NET modules

# https://docs.microsoft.com/en-us/dotnet/api/system?view=netcore-3.1
import System
print dir(System.Collections)
help(System.Collections.ArrayList)

# https://docs.python.org/3/library/sys.html
import sys
print dir(sys)
help(sys)



#----Samples of dir() and help() with Rhino specific Python modules

# https://developer.rhino3d.com/api/RhinoScriptSyntax/
import rhinoscriptsyntax as rs
print dir(rs)
help(rs.Command)

# No API documentation found online
import scriptcontext as sc
print dir(sc)
help(sc.doc)

# https://developer.rhino3d.com/api/RhinoCommon/html/R_Project_RhinoCommon.htm
import Rhino as rh
print dir(rh)
print dir(rh.DocObjects)
print dir(rh.DocObjects.Tables)
print dir(rh.DocObjects.Tables.ObjectTable)
help(rh.DocObjects.Tables.ObjectTable.Delete)