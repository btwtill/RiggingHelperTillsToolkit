import maya.cmds as mc



def reloadShelf():
    import RiggingHelperTillsToolkit
    import importlib
    importlib.reload(RiggingHelperTillsToolkit)
    from RiggingHelperTillsToolkit import shelf_base
    importlib.reload(shelf_base)
    test = shelf_base.customShelf()