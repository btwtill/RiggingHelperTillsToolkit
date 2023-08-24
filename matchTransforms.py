
import maya.cmds as mc


def matchAll():
    selection = mc.ls(selection=True)
    print(selection)
    if len(selection) >= 2:
        targetMatrix = mc.xform(selection[-1], query=True, worldSpace=True, matrix=True)
        print(targetMatrix)
        for i in range(len(selection)):
            if i != (len(selection) - 1):
                mc.xform(selection[i], worldSpace=True, matrix=targetMatrix)
                print(i)




def matchTranslation():
    selection = mc.ls(selection=True)
    if len(selection) >= 2:
        targetTranslation = mc.xform(selection[-1], query=True, worldSpace=True, translation=True)
        for i in range(len(selection)):
            if i != (len(selection) - 1):
                mc.xform(selection[i], worldSpace=True, translation=targetTranslation)




def matchRotation():
    selection = mc.ls(selection=True)
    if len(selection) >= 2:
        rotationTarget = mc.xform(selection[-1], query=True, worldSpace=True, rotation=True)
        for i in range(len(selection)):
            if i != (len(selection) - 1):
                mc.xform(selection[i], worldSpace=True, rotation=rotationTarget)


def matchScale():
    selection = mc.ls(selection=True)
    if len(selection) >= 2:
        scaleTarget = mc.xform(selection[-1], query=True, worldSpace=True, scale=True)
        for i in range(len(selection)):
            if i != (len(selection) - 1):
                mc.xform(selection[i], worldSpace=True, scale=scaleTarget)