"""
Python template for Rhino and Grasshopper.
"""

__author__ = "Darrel Ronald"
__version__ = "2020"

#----Import .NET Assemblies
#https://ironpython.net/documentation/dotnet/dotnet.html
#import clr
#clr AddReference(".Net assemply")

#----Import .NET Modules
#import sys
#import System
#import System.Guid

#----Import Rhino Modules
#import rhinoscriptsyntax as rs
#rs.Command("_NameOfCommand")
#import ghpythonlib.components as ghcomp
#import ghpythonlib.parallel as ghp
#import scriptcontext as sc
#import Rhino
#import Rhino.DocObjects as rhdoc
#import Rhino.NodeInCode.Components as ghnodes
#import Rhino.Geometry as rg

#----Setting Context of script and rhino doc
# set the active RhinoDoc before interacting with Rhino
#sc.doc = Rhino.RhinoDoc.ActiveDoc
# set the gh Script back to Grasshoper after interacting with Rhino
#sc.doc = ghdoc