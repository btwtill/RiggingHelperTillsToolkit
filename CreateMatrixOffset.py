import maya.cmds as mc


def iterateCreateMatrixZeroOffset():
    sel = mc.ls(selection=True)
    createMatrixZeroOffset(sel[0])


def createMatrixZeroOffset(sel):
    #zero Node Input
    zro_node = mc.pickWalk(direction="up")
    
    #get parent Node Input
    parent_node = mc.listRelatives(zro_node, parent=True)
    
    
    #create zro Matrix
    zro_mtrx = mc.rename(mc.createNode("composeMatrix"), zro_node[0] + "_mtrx")
    
    #set translation
    mc.setAttr(zro_mtrx + ".inputTranslateX", mc.getAttr(zro_node[0] + ".translateX"))
    mc.setAttr(zro_mtrx + ".inputTranslateY", mc.getAttr(zro_node[0] + ".translateY"))
    mc.setAttr(zro_mtrx + ".inputTranslateZ", mc.getAttr(zro_node[0] + ".translateZ"))
    
    #set rotation
    mc.setAttr(zro_mtrx + ".inputRotateX", mc.getAttr(zro_node[0] + ".rotateX"))
    mc.setAttr(zro_mtrx + ".inputRotateY", mc.getAttr(zro_node[0] + ".rotateY"))
    mc.setAttr(zro_mtrx + ".inputRotateZ", mc.getAttr(zro_node[0] + ".rotateZ"))
    
    #set scale
    mc.setAttr(zro_mtrx + ".inputScaleX", mc.getAttr(zro_node[0] + ".scaleX"))
    mc.setAttr(zro_mtrx + ".inputScaleY", mc.getAttr(zro_node[0] + ".scaleY"))
    mc.setAttr(zro_mtrx + ".inputScaleZ", mc.getAttr(zro_node[0] + ".scaleZ"))
    
    #create multMatrix
    mult_mtrx = mc.rename(mc.createNode("multMatrix"), zro_mtrx + "_mult")
    
    #connect zro mtrx to multMatrix
    mc.connectAttr(zro_mtrx + ".outputMatrix", mult_mtrx + ".matrixIn[0]")
    
    #connect parent worldmatrix to mult matirx 
    if parent_node:
        mc.connectAttr(parent_node[0] + ".worldMatrix[0]", mult_mtrx + ".matrixIn[1]")
    else:
        origin_mtrx = mc.rename(mc.createNode("composeMatrix"), "Origin_mtrx")
        mc.connectAttr(origin_mtrx + ".outputMatrix", mult_mtrx + ".matrixIn[1]")
    
    #connect outmatrix to selected transform
    mc.connectAttr(mult_mtrx + ".matrixSum", sel + ".offsetParentMatrix")
    
    #unparent selected transform 
    mc.parent(sel, world=True)
    
    mc.delete(zro_node)
    
    #zero out selected transforms transfrom channels
    mc.setAttr(sel + ".translateX", 0)
    mc.setAttr(sel + ".translateY", 0)
    mc.setAttr(sel + ".translateZ", 0)
    
    mc.setAttr(sel + ".rotateX", 0)
    mc.setAttr(sel + ".rotateY", 0)
    mc.setAttr(sel + ".rotateZ", 0)
    
    mc.setAttr(sel + ".scaleX", 1)
    mc.setAttr(sel + ".scaleY", 1)
    mc.setAttr(sel + ".scaleZ", 1)



