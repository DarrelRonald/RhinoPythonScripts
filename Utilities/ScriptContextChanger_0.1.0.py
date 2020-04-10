"""Script Context Changer.
    Inputs:
        ScriptContext: Your chosen script context
    Output:
        ActiveContext: The active script context"""
__author__ = "Darrel Ronald"
__version__ = "2020"


#----imports
import Rhino as rh
import rhinoscriptsyntax as rs
import scriptcontext as sc

# set ScriptContext to Rhino where sc.id = 1
sc.doc = sc.id = 1 
whatContext = rs.ContextIsRhino()
print whatContext
print sc.id

# set ScriptContext to Grasshopper where sc.id = 2
sc.doc = sc.id = 2
whatContext = rs.ContextIsGrasshopper()
print whatContext
print sc.id

ActiveContext = sc.id