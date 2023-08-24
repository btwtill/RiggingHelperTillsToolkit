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


#Tim Zero


def TimZeroUserConfig():

    #basic Window creation
    configWindow = mc.window(title="IKFKSwitch", iconName='IKFK', widthHeight=(200, 55), sizeable=True)
    
    #Window Layout
    mc.rowColumnLayout( adjustableColumn=True )
    
    #Label
    mc.text( label='Offset Nodes' )
    
    #Input Field Sotring the Stirng value
    grp = mc.checkBox(label="_grp", value=True)
    offs = mc.checkBox(label="_off")
    drv = mc.checkBox(label="_drv")
    
    #Building the switch execution button
    mc.button( label='create Offset Nodes', command=lambda _: TimZero(mc.ls(selection=True), assembleOffsetList(mc.checkBox(grp, query=True, value=True), 
                                                                                                                mc.checkBox(offs, query=True, value=True),
                                                                                                                mc.checkBox(drv, query=True, value=True))))

    #Display The window
    mc.showWindow(configWindow)

def assembleOffsetList(_grp, _offs, _drv):
    offsetList = []

    if _grp:
        offsetList.append('_grp')
    if _offs:
        offsetList.append("_off")
    if _drv:
        offsetList.append("_drv")
    print(offsetList)
    return offsetList


def TimZero(transform_list, add_transforms):
    for tfm in transform_list:
        if mc.nodeType(tfm) == 'transform':
            created_tfms = list()
            for i in range(0, len(add_transforms)):
                add_tfm = mc.duplicate(tfm, po=True, name= tfm + add_transforms[i])
                created_tfms.append(add_tfm)
                if i:
                    mc.parent(add_tfm, created_tfms[i - 1])
            mc.parent(tfm, created_tfms[-1])
                    
        else:
            print ('No not a tranform')

############################