import maya.cmds as mc
from RiggingHelperTillsToolkit import shelf_base


def reloadShelf():
    try:
        from imp import reload
        from RiggingHelperTillsToolkit import shelf_base

        reload(shelf_base)

        shelf_base.customShelf()
        print("Succesful Reload")
    except:
        log.error("Error reloading shelf")
        return