# RhinoPython and ghPyton Scripts
Scripts for use in Rhino 3D and Grasshopper. These are public scripts that can perhaps be of use in day-to-day projects and learning. 

What has been especially frustrating for me when learning scripting within the context of Rhino3D and Grasshopper3D is the many different ways to do the same things. For example, you can create the same script functionality in Python by using `scriptcontext` versus `RhinoCommon` versus `rhinoscriptcontext`. This flexibility is both good and bad, because it simplifies some things, but creates confusion around what is the best method to write scripts. In addition, each of the methods has pros/cons that need workarounds. For example, the `rhinoscriptsyntax` is simpler for writing scripts, but the API is incomplete. 

Further frustrating in the learning process is about understanding and using the `.NET` framework, `IronPython` and how to work with `.NET Assemblies`. The Microsoft documentation is very difficult to understand, there are many different versions of `.NET` and McNeel doesn't offer any guides or overviews (that I know of) to work with these libraries. 

For many of the ghPython scripts we only need proedural programming, but the class-oriented and object-oriented programming of the .NET environment and the McNeel [Rhino Developer Examples](https://github.com/mcneel/rhino-developer-samples/tree/5c8ac43e6d679125f08b5713ff1ac311819acd49) make learning more confusing for non-professional coders.

## Learning
* __Add-Delete-Circle.py__ (includes: .py): this is a modification of the `add-circle.py` code of McNeel to see the 2 different methods of writing the `circle()` class and also to compare 2 ways to delete objects within the Rhino3D file using either `scriptcontext` versus `RhinoCommon` versus `rhinoscriptcontext`. One article I found after all this exploration was by [Danil Nagy](https://medium.com/generative-design/working-with-geometry-in-python-a256de7bb1b1)-however, the one mistake he makes is writing `Rhino.Geometry` instead of the correct `"Rhino"` library. Rhino.Geometry only gives you access to that specific Geometry Namespace.

## Utilities
* __ListOfRhinoCommands__ (includes: .py, .gha): this sorts a list of all `Rhino.Commands` that can be accessed through RhinoCommon. It is a tool for seeing quickly what commands are available. You can also copy the output panel contents and paste into an excel sheet.
* __ScriptContextChanger__ (includes different: .py, .gha): these are more educational code blocks. However, if you're writing python scripts using RhinoCommon, you will sometimes need to change the `scriptcontext.doc`
* __ImportSysExplorer_0.1.0__ (includes: .gha): This ghPython module imports the sys module from IronPython and exports to panels both `sys.builtin_module_names` and the `sys.path`.
* __PythonTemplate_0.1.0__ (includes: .py): This python script has the most important python template elements.
