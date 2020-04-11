"""
This script aims to show the different styles of deleting objects in Rhino. 
"""
import Rhino
import scriptcontext as sc
import System.Guid
import rhinoscriptsyntax as rs

def AddCircle():  # Written by McNeel
    center = Rhino.Geometry.Point3d(0, 0, 0)
    radius = 10.0
    c = Rhino.Geometry.Circle(center, radius)
   
    if sc.doc.Objects.AddCircle(c)!=System.Guid.Empty:
        sc.doc.Views.Redraw()
        return Rhino.Commands.Result.Success
    return Rhino.Commands.Result.Failure

def AddCircle2():  # Written by Darrel Ronald
    center = Rhino.Geometry.Point3d(5, 5, 5)
    radius = 20.0
    c = Rhino.Geometry.Circle(center, radius)
    sc.doc.Objects.AddCircle(c)
    sc.doc.Objects.AddPoint(center)
    sc.doc.Views.Redraw()


if __name__=="__main__":

    AddCircle2()
    #----Option Rhinoscriptsyntax
    id = rs.AllObjects(select=True)
    rs.DeleteObjects(id)
    
    AddCircle()
    
    #---- Option Scriptcontext
    sc.doc.Objects.Clear()
    
    AddCircle2()
    