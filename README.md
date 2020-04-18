# RhinoPython and ghPyton Scripts
Scripts for use in Rhino 3D and Grasshopper. These are public scripts that can perhaps be of use in day-to-day projects and learning. 

What has been especially frustrating for me when learning scripting within the context of Rhino3D and Grasshopper3D is the many different ways to do the same things. For example, you can create the same script functionality in Python by using `scriptcontext` versus `RhinoCommon` versus `rhinoscriptcontext`. This flexibility is both good and bad, because it simplifies some things, but creates confusion around what is the best method to write scripts. In addition, each of the methods has pros/cons that need workarounds. For example, the `rhinoscriptsyntax` is simpler for writing scripts, but the API is incomplete. 

Further frustrating in the learning process is about understanding and using the `.NET` framework, `IronPython` and how to work with `.NET Assemblies`. The Microsoft documentation is very difficult to understand, there are many different versions of `.NET` and McNeel doesn't offer any guides or overviews (that I know of) to work with these libraries. 

For many of the ghPython scripts we only need proedural programming, but the class-oriented and object-oriented programming of the .NET environment and the McNeel [Rhino Developer Examples](https://github.com/mcneel/rhino-developer-samples/tree/5c8ac43e6d679125f08b5713ff1ac311819acd49) make learning more confusing for non-professional coders.

## Learning Scripts/Components
* __Add-Delete-Circle.py__ (includes: .py): this is a modification of the `add-circle.py` code of McNeel to see the 2 different methods of writing the `circle()` class and also to compare 2 ways to delete objects within the Rhino3D file using either `scriptcontext` versus `RhinoCommon` versus `rhinoscriptcontext`. One very good article I found after all this exploration was by [Danil Nagy](https://medium.com/generative-design/working-with-geometry-in-python-a256de7bb1b1)-however, the one mistake he makes is writing `Rhino.Geometry` instead of the correct `Rhino` library. `Rhino.Geometry` only gives you access to that specific Geometry Namespace.
* __Dir-Help.py__ (includes: .py): this is an example of how to use the builtin python functions `dir()` and `help()` when learning about new Python or RhinoPython modules while you're writing scripts. It can be used in your IDE as an alternative to looking up the API documentation online, which in some cases doesn't exist.
* __GetIronPythonModules.py__ (includdes: .py, .gh): This allows you to see all importable modules as well as a selected `sys.path` directory because sometimes the Rhino Python Editor Intellisense doesn't recognize all the IronPython modules. This allows you to see what Rhino will recognize. Thanks to [Anders Deleuran](https://discourse.mcneel.com/u/AndersDeleuran) for helping me with this on this [McNeel Discourse thread](https://discourse.mcneel.com/t/importing-ironpython-libraries/100288).

## Utility Scripts/Components
* __ListOfRhinoCommands__ (includes: .py, .gh): this sorts a list of all `Rhino.Commands` that can be accessed through RhinoCommon. It is a tool for seeing quickly what commands are available. You can also copy the output panel contents and paste into an excel sheet.
* __ScriptContextChanger__ (includes different: .py, .gh): these are more educational code blocks. However, if you're writing python scripts using RhinoCommon, you will sometimes need to change the `scriptcontext.doc`
* __ImportSysExplorer_0.1.0__ (includes: .gh): This ghPython module imports the sys module from IronPython and exports to panels both `sys.builtin_module_names` and the `sys.path`.
* __PythonTemplate_0.1.0__ (includes: .py): This python script has the most important python template elements.


# Tips & Tricks
Below are some things that I've noticed along the way, read up on the Discourse forum and know that others will probably find these same challenges, bugs or frustrations.

1. __Rhino Python Intellisense__: In a Python script, sometimes the builtin Rhino Python Editor (both Rhino and Grasshopper) won't recognize the full set of IronPython modules. Other people also had this problem. You can `import` the modules you want, and intellisense should start working after it has been imported. I had this problem on Window 10, Rhino v6 SR 24. In the above __Learning__ section you will see the script `GetIronPythonModules.py` you can see the full list of importable modules from Rhino Python.
1. __Rhino Python IDE with PyCharm__: [Steve Baer has an article](https://stevebaer.wordpress.com/2019/02/25/autocomplete-and-type-hints-with-python-scripts-for-rhino-grasshopper/) explaining how to use [PyCharm](https://www.jetbrains.com/pycharm/) with intellisense stubs for RhinoCommon and Grasshopper.
