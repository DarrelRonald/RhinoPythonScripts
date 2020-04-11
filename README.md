# RhinoPython and ghPyton Scripts
Scripts for use in Rhino 3D and Grasshopper.
These are public scripts that can perhaps be of use in day-to-day projects and learning.<br/>
What has been especially frustrating for me when learning scripting within the context of Rhino3D and Grasshopper3D is the many different ways to do the same things. Further frustrating is the whole learning process around the `.NET` framework and the class-oriented object-oriented programming of the McNeel examples.

## Learning
* __Add-Delete-Circle.py__ (includes: .py): this is a modification of the `add-circle.py` code of McNeel to see the 2 different methods of writing the `circle()` class and also to compare 2 ways to delete objects within the Rhino3D file using either `scriptcontext` versus `RhinoCommon` and `rhinoscriptcontext`.

## Utilities
* __ListOfRhinoCommands__ (includes: .py, .gha): this sorts a list of all `Rhino.Commands` that can be accessed through RhinoCommon. It is a tool for seeing quickly what commands are available. You can also copy the output panel contents and paste into an excel sheet.
* __ScriptContextChanger__ (includes different: .py, .gha): these are more educational code blocks. However, if you're writing python scripts using RhinoCommon, you will sometimes need to change the `scriptcontext.doc`
* __ImportSysExplorer_0.1.0__ (includes: .gha): This ghPython module imports the sys module from IronPython and exports to panels both `sys.builtin_module_names` and the `sys.path`.
* __PythonTemplate_0.1.0__ (includes: .py): This python script has the most important python template elements.
