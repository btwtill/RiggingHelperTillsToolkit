# TestFuncitons
 Multiple Helper Functions for Rigging Use



TODO
    Split code into Modules


First shelf Install 

    import RiggingHelperTillsToolkit
    import importlib
    importlib.reload(RiggingHelperTillsToolkit)
    from RiggingHelperTillsToolkit import shelf_base
    importlib.reload(shelf_base)
    test = shelf_base.customShelf()


userSetup.py - entry

import maya.cmds as mc
import maya.utils

import RiggingHelperTillsToolkit.shelf_base as shelf
mc.evalDeferred("shelf.customShelf()")










sel = cmds.ls(selection=True)
ctrlListTarget = "_CTRL"
jointListTarget = "_JNT"

filteredCtrlList = [s for s in sel if ctrlListTarget in s] 
filteredJntList = [s for s in sel if jointListTarget in s]



for i in sel:
    cmds.rename(i, i + '_JNT')