import maya.cmds as mc


##ShapeParent Function 
def ShapeParent(*args):
    selection = mc.ls(selection=True)
    PosOffset = True

    if(selection):
        mc.parent(selection[0], selection[1], shape=True, relative=PosOffset)
############################


##ShapeNode Instance
def shapeParentInstance():
    selectionList = mc.ls(selection=True)
    instanceNode = ""
    for i in range(len(selectionList)):
        print(selectionList[i])
        if i == 0:
            instanceNode = selectionList[i]
            print(instanceNode)
        else:
            mc.parent(instanceNode, selectionList[i], add=True, shape=True)






##Sam Zero Functionality 
def insertNodeBefore(sfx = '_zro', alignToParent = False, loc = False, replace = '_ctl'):
    nodes = mc.ls(sl = 1)

    isRoot = False
    cnNodes = []
    for node in nodes:
        zName = node
        # if we add a zero to a ctl, kill the suffix
        if replace in node:
            zName = node.replace(replace, '')

        # create in between node
        if loc:
            cnNode = mc.spaceLocator( n = zName + sfx)[0]
        else:
            cnNode = mc.createNode('transform', n = zName + sfx)

        # get parent
        nodeParent = mc.listRelatives(node, p = True)


        if nodeParent == None:
            if alignToParent:
                print ('Do Nothing, world parented')
            else:
                mc.matchTransform(cnNode, node)
        else:
            if alignToParent:
                mc.matchTransform(cnNode, nodeParent)
            else:
                mc.matchTransform(cnNode, node)
            mc.parent(cnNode, nodeParent)

        mc.parent(node, cnNode)
        cnNodes.append(cnNode)

        # check if we have are zeroeing a joint (because if so we need to zero out all Orients)
        if not alignToParent:
            if mc.objectType(node, isType = 'joint'):
                for attr in ('.rx', '.ry', '.rz', '.jointOrientX', '.jointOrientY', '.jointOrientZ'):
                    mc.setAttr(node+attr, 0)

    return cnNodes
############################




# sel = cmds.ls(selection=True)

# qshape = cmds.curve(p=[(0,0,0), (0,0,0)])


# qshape = cmds.rename(qshape, sel[0] + '_q')
# cmds.select(qshape)

# selectionShape = cmds.pickWalk(direction="Down")


# cmds.parent(selectionShape, sel[0], shape=True, relative=True)

# multmatrix = cmds.createNode('multMatrix')
# decomposeMatrix = cmds.createNode('decomposeMatrix')


# cmds.connectAttr(multmatrix + '.matrixSum', decomposeMatrix + '.inputMatrix')

# cmds.connectAttr(sel[1] + '.worldMatrix', multmatrix + '.matrixIn[0]')
# cmds.connectAttr(sel[0] + '.worldInverseMatrix[0]', multmatrix + '.matrixIn[1]')


# cmds.connectAttr(decomposeMatrix + '.outputTranslateX', selectionShape[0] + '.controlPoints[0].xValue')
# cmds.connectAttr(decomposeMatrix + '.outputTranslateY', selectionShape[0] + '.controlPoints[0].yValue')
# cmds.connectAttr(decomposeMatrix + '.outputTranslateZ', selectionShape[0] + '.controlPoints[0].zValue')

# cmds.delete(qshape)
