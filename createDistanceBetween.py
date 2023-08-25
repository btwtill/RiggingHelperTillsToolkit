import maya.cmds as mc


def createDistance():
    sel = mc.ls(selection=True)

    distNode = mc.createNode("distanceBetween")

    mc.connectAttr(sel[0] + ".worldMatrix[0]", distNode + ".inMatrix1")
    mc.connectAttr(sel[1] + ".worldMatrix[0]", distNode + ".inMatrix2")