import maya.cmds as mc
from RiggingHelperTillsToolkit import shelf_base


def reloadShelf():
    import importlib
    importlib.reload(shelf_base)
    shelf_base.customShelf()