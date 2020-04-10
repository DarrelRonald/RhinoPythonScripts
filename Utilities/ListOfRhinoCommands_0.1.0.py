"""Generate a sorted list of Rhino Commands.
    Inputs:
        run: bool to set True (to run) or False
    Output:
        commands: a sorted list of all Rhino Commands"""

__author__ = "Darrel Ronald"
__version__ = "0.1.0"

import Rhino

commands = []

if run == True:
    commands = Rhino.Commands.Command.GetCommandNames(True, False)
    commands = sorted(commands)