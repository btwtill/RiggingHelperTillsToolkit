import maya.cmds as mc


##DO NOTHING FUNCTION Base function used for passing a default action into a created button without command argument
def _null(*args):
    pass

##Base Shelf class with building block functions used for building your custom shelf
class _shelf():
    '''A simple class to build shelves in maya. Since the build method is empty,
    it should be extended by the derived class to build the necessary shelf elements.
    By default it creates an empty shelf called "customShelf".'''

    def __init__(self, name="RHF", iconPath=""):
        self.name = name

        self.iconPath = iconPath

        self.labelBackground = (0, 0, 0, 0)
        self.labelColour = (.9, .9, .9)

        self._cleanOldShelf()
        mc.setParent(self.name)
        self.build()

    def build(self):
        '''This method should be overwritten in derived classes to actually build the shelf
        elements. Otherwise, nothing is added to the shelf.'''
        pass

    def addButton(self, label, icon="commandButton.png", command=_null, doubleCommand=_null):
        '''Adds a shelf button with the specified label, command, double click command and image.'''
        mc.setParent(self.name)
        if icon:
            icon = self.iconPath + icon
        mc.shelfButton(width=37, height=37, image=icon, l=label, command=command, dcc=doubleCommand, imageOverlayLabel=label, olb=self.labelBackground, olc=self.labelColour)

    def addMenuItem(self, parent, label, command=_null, icon=""):
        '''Adds a shelf button with the specified label, command, double click command and image.'''
        if icon:
            icon = self.iconPath + icon
        return mc.menuItem(p=parent, l=label, c=command, i="")

    def addSubMenu(self, parent, label, icon=None):
        '''Adds a sub menu item with the specified label and icon to the specified parent popup menu.'''
        if icon:
            icon = self.iconPath + icon
        return mc.menuItem(p=parent, l=label, i=icon, subMenu=1)

    def _cleanOldShelf(self):
        '''Checks if the shelf exists and empties it if it does or creates it if it does not.'''
        if mc.shelfLayout(self.name, ex=1):
            if mc.shelfLayout(self.name, q=1, ca=1):
                for each in mc.shelfLayout(self.name, q=1, ca=1):
                    mc.deleteUI(each)
        else:
            mc.shelfLayout(self.name, p="ShelfLayout")

############################ Base Shelf End ############################




##Custom schelf buildl process add all the function you wannt into this function in order to build the shelf
class customShelf(_shelf):
    def build(self):
        self.addButton(label="Test_Run", command=Run_Test)
        self.addButton(label="ShapeParent", command=ShapeParent)
        self.addButton(label="SamZero", command=insertNodeBefore)
        self.addButton(label="IKFKSwitch", command=IKFKConfigurationInterface)

############################ Custom Shelf End ############################









##Functions to populate the shelf








##ShapeParent Function 
def ShapeParent(*args):
    selection = mc.ls(selection=True)
    PosOffset = True

    if(selection):
        mc.parent(selection[0], selection[1], shape=True, relative=PosOffset)
############################






##Test Function
def Run_Test():
    print("Successful Installation")
############################






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



## IK FK Switch Functionallity


#Function to turn Joint Selection into IKFK Switch
def IKFKSwitch(doParentJointCreation, _selectionList):
        selectionList = _selectionList

        def duplicateSelection(selectionArray):
                dupList = []
                for i in selectionArray:
                    newJoint = mc.duplicate(i, parentOnly=True)
                    try:
                        mc.parent(newJoint, world=True)
                    except:
                        print("already world Parent")
                    dupList.append(newJoint)
                    
                return dupList
            
        def renameList(targetList, name):
            renamedList = []
            for i in range(len(targetList)):
                listElement = "".join(targetList[i])
                newName = listElement.replace("1", "")
                newName = name + newName
                renamedList.append(newName)
                mc.rename(targetList[i], newName)
            return renamedList


        def reparenting(targetArray):
            for i in range(len(targetArray)):
                if i != (len(targetArray) - 1):
                    mc.parent(targetArray[i + 1], targetArray[i])
                
        def createIKChain(targetChain):
            mc.select(targetChain[0], targetChain[len(targetChain) - 1])
            IkHanldeName = "".join(targetChain[len(targetChain) - 1]) + "_IK_Handle"
            mc.ikHandle(targetChain[0], targetChain[len(targetChain) - 1], name=IkHanldeName)

        def createIKFKSwitch(iKChain, fKChain, targetChain):
            for i in range(len(targetChain)):
                currentBlendNode = mc.pairBlend(node=targetChain[i], attribute=["tx", "ty", "tz", "rx", "ry", "rz"])
                
                ikNodeTranslationX = iKChain[i] + ".translateX"
                ikNodeTranslationY = iKChain[i] + ".translateY"
                ikNodeTranslationZ = iKChain[i] + ".translateZ"
                
                ikNodeRotationX = iKChain[i] + ".rotateX"
                ikNodeRotationY = iKChain[i] + ".rotateY"
                ikNodeRotationZ = iKChain[i] + ".rotateZ"
                
                fkNodeTranslationX = fKChain[i] + ".translateX"
                fkNodeTranslationY = fKChain[i] + ".translateY"
                fkNodeTranslationZ = fKChain[i] + ".translateZ"
                
                fkNodeRotationX = fKChain[i] + ".rotateX"
                fkNodeRotationY = fKChain[i] + ".rotateY"
                fkNodeRotationZ = fKChain[i] + ".rotateZ"
                
                currentBlendNodeTranslateX1 = currentBlendNode + ".inTranslateX1"
                currentBlendNodeTranslateY1 = currentBlendNode + ".inTranslateY1"
                currentBlendNodeTranslateZ1 = currentBlendNode + ".inTranslateZ1"
                
                currentBlendNodeRotationX1 = currentBlendNode + ".inRotateX1"
                currentBlendNodeRotationY1 = currentBlendNode + ".inRotateY1"
                currentBlendNodeRotationZ1 = currentBlendNode + ".inRotateZ1"
                
                
                currentBlendNodeTranslateX2 = currentBlendNode + ".inTranslateX2"
                currentBlendNodeTranslateY2 = currentBlendNode + ".inTranslateY2"
                currentBlendNodeTranslateZ2 = currentBlendNode + ".inTranslateZ2"
                
                currentBlendNodeRotationX2 = currentBlendNode + ".inRotateX2"
                currentBlendNodeRotationY2 = currentBlendNode + ".inRotateY2"
                currentBlendNodeRotationZ2 = currentBlendNode + ".inRotateZ2"
                
                mc.connectAttr(ikNodeTranslationX, currentBlendNodeTranslateX1)
                mc.connectAttr(ikNodeTranslationY, currentBlendNodeTranslateY1)
                mc.connectAttr(ikNodeTranslationZ, currentBlendNodeTranslateZ1)
                
                mc.connectAttr(ikNodeRotationX, currentBlendNodeRotationX1)
                mc.connectAttr(ikNodeRotationY, currentBlendNodeRotationY1)
                mc.connectAttr(ikNodeRotationZ, currentBlendNodeRotationZ1)
                
                mc.connectAttr(fkNodeTranslationX, currentBlendNodeTranslateX2)
                mc.connectAttr(fkNodeTranslationY, currentBlendNodeTranslateY2)
                mc.connectAttr(fkNodeTranslationZ, currentBlendNodeTranslateZ2)
                
                mc.connectAttr(fkNodeRotationX, currentBlendNodeRotationX2)
                mc.connectAttr(fkNodeRotationY, currentBlendNodeRotationY2)
                mc.connectAttr(fkNodeRotationZ, currentBlendNodeRotationZ2)

##Check if Joints are Selected
        if len(selectionList) >= 2:
            
            ##Create the Chains

            #FK Joints
            fkArray = duplicateSelection(selectionList)
            fkArray = renameList(fkArray, "FK_")

            #IK Joints
            ikArray = duplicateSelection(selectionList)
            ikArray = renameList(ikArray, "IK_")

            #Reparent the individual Joints into Chains
            reparenting(fkArray)
            reparenting(ikArray)

            #Create IK System
            createIKChain(ikArray)

            #Build the Switch
            createIKFKSwitch(ikArray, fkArray, selectionList)

            if doParentJointCreation:
                CreateANCORParent(selectionList, ikArray, fkArray)
       
        else:
            print("Select Joints")


##Create an IKFK Attribute for switching between ik and fk
def createIKFKAttribute(IKFKattributeName):
    attribute = mc.spaceLocator()
    mc.select(attribute)
    addedAttributeName = "".join(mc.pickWalk(direction="down")) + "." + IKFKattributeName
    mc.addAttr(longName=IKFKattributeName, minValue=0, maxValue=1, defaultValue=0)
    mc.setAttr(addedAttributeName, keyable=True)
    mc.rename("iKfK")


##Create Anchor and Parent Bone for IKFK Chain
def CreateANCORParent(_selectionForAnchor, _ikArray, _fkArray):

    selectionList = _selectionForAnchor

    #selet target Joint
    mc.select(selectionList[0])
    parentJoint = mc.pickWalk(direction="up")

    #create list to keep track of the names
    tmpParentingChainList = [parentJoint]

    #duplicate target joint rename it and add it to the list
    targetDuplicate = mc.duplicate(parentJoint, parentOnly=True)
    targetDuplicateName = "".join(targetDuplicate)
    targetDuplicateName = "IKFK_" + targetDuplicateName.replace("1", "") 
    targetDuplicate = mc.rename(targetDuplicate, targetDuplicateName)
    tmpParentingChainList.append(targetDuplicateName)

    #unparent it
    mc.parent(targetDuplicate, world=True)

    #constrain it back to tha target joint
    mc.parentConstraint(tmpParentingChainList[0], tmpParentingChainList[1])

    #parent the IK FK Chains to the IKFK Parent Joint
    mc.parent(_ikArray[0], tmpParentingChainList[1])
    mc.parent(_fkArray[0], tmpParentingChainList[1])

    #store pos for Anchor
    ChainPos = mc.xform(selectionList[0], query=True, worldSpace=True, translation=True)

    #create, move and parent the Anchor
    Anchor = mc.spaceLocator(name=selectionList[0] + "_ACNHOR")
    mc.xform(Anchor, worldSpace=True, translation=ChainPos)
    mc.parent(Anchor, tmpParentingChainList[0])

##Function to connect an attribute to multiple pair blend Weight attributes  
def ConnectPairBlend(_attribute_name):

    selectionList = mc.ls(selection=True)
    
    for i in range(len(selectionList)):
        weightOutPut = ""
        if i == 0:
            weightOutput = selectionList[i]
            weightOutput = weightOutput + "." + _attribute_name
        else:
            input = selectionList[i] + ".weight"
            mc.connectAttr(weightOutput, input)



##build function deciding what will be executed
def BuildSwitch(args, parentJointCreation, attributeShapeCreation, switchCreation):
    
    selectionList = mc.ls(selection=True)

    if attributeShapeCreation:
        createIKFKAttribute(args)
    if switchCreation:
        IKFKSwitch(parentJointCreation, selectionList)
    
       
#Open Dialogue to Create the IKFK Switch
def IKFKConfigurationInterface():
    
    #basic Window creation
    configWindow = mc.window(title="IKFKSwitch", iconName='IKFK', widthHeight=(200, 55), sizeable=True)
    
    #Window Layout
    mc.rowColumnLayout( adjustableColumn=True )
    
    #Label
    mc.text( label='Attribute_Name' )
    
    #Input Field Sotring the Stirng value
    name = mc.textField()
    
    #Bool If the Attribute Shape should be created
    doCreateAttributeShape = mc.checkBox(label="Create Attribute Shape")
    
    #Bool to enable creating the parent joint for the IK FK Switch Joints
    doCreateParentJoint = mc.checkBox(label="ParnetJoint")
    
    #Bool to create the switch
    doCreateSwitch = mc.checkBox(label="Create Switch", value=True)
    
    #Building the switch execution button
    mc.button( label='Build Swtich', command=lambda _: BuildSwitch(mc.textField(name, query=True, text=True), mc.checkBox(doCreateParentJoint, query=True, value=True), mc.checkBox(doCreateAttributeShape, query=True, value=True), mc.checkBox(doCreateSwitch, query=True, value=True)))
    
    #Input Field to determin which Attribute should be connected to the weight inputs on the pair blend Nodes
    ikfkAttributeName = mc.textField()

    #execution button to connect the ikfk Attribute with the blend Nodes
    mc.button( label='ConnectPairBlends', command=lambda _: ConnectPairBlend(mc.textField(ikfkAttributeName, query=True, text=True)))

    #Display The window
    mc.showWindow(configWindow)
    
############################ IK FK Functionality End ############################
