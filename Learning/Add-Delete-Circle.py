"""
This script aims to show the different styles of deleting objects in Rhino. 
"""
import Rhino
import scriptcontext as sc
import System.Guid
import rhinoscriptsyntax as rs

# addCircle written by McNeel
def AddCircle():  
    center = Rhino.Geometry.Point3d(0, 0, 0)
    radius = 10.0
    c = Rhino.Geometry.Circle(center, radius)
   
    if sc.doc.Objects.AddCircle(c)!=System.Guid.Empty:
        sc.doc.Views.Redraw()
        return Rhino.Commands.Result.Success
    return Rhino.Commands.Result.Failure

 # addCircle rewritten to see what is necessary
def AddCircle2(): 
    center = Rhino.Geometry.Point3d(5, 5, 5)
    radius = 20.0
    c = Rhino.Geometry.Circle(center, radius)
    sc.doc.Objects.AddCircle(c)
    sc.doc.Objects.AddPoint(center)
    sc.doc.Views.Redraw()


if __name__=="__main__":

    # Add geometry to delete
    AddCircle2()
    
    #----Option "Delete" using Rhinoscriptsyntax
    id = rs.AllObjects(select=True)
    rs.DeleteObjects(id)
    
    # Add geometry to delete
    AddCircle()
    
    #---- Option "Delete" using Scriptcontext
    sc.doc.Objects.Clear()
    
    # Add geometry to delete
    AddCircle()
    AddCircle2()
    

    #--- Option "Delete" using RhinoCommon
    ot = rs.AllObjects(select=True) #Rhino.RhinoDoc.ActiveDoc.Objects
    ot_id = []
    
    def idMaker(objects):
        for i in ot:
           Rhino.DocObjects.RhinoObject.Id
           ot_id.append(i)
    idMaker(ot)
    Rhino.RhinoDoc.ActiveDoc.Objects.Delete(ot_id, True)


    # Add geometry to delete
    AddCircle2()