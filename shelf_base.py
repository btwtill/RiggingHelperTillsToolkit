import maya.cmds as mc

from RiggingHelperTillsToolkit import IkFkFunctions, ParentingFunctions, ColorFunctions, NamingFunctions, PoleVectorLineFunctions, ReverseFoot, CreateControlsFunction, MatrixOffset, MultiConnect, SamStretchSetup, addTwistJointsFunction, JiggleSetup, shelfReload, matchTransforms, SimplePoleVector, CreateMatrixOffset, createDistanceBetween


##ICON DIRECTORY
ICON_DIR="C:/Users/Remote/Documents/maya/scripts/RiggingHelperTillsToolkit/icons"

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
    
    def addMenuItemDivider(self, parent, divider=True, dividerLabel=""):
        """Adds a shelf button with the specified label, command, double click command and image."""
        return mc.menuItem(p=parent, divider=divider, dividerLabel=dividerLabel)

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
        self.addButton(label="", icon=ICON_DIR + "/test.png" ,command=Run_Test)

        self.addButton(label="", icon=ICON_DIR + "/sep.png")

        self.addButton(label="", icon=ICON_DIR + "/reload.png" ,command=shelfReload.reloadShelf)

        self.addButton(label="", icon=ICON_DIR + "/sep.png")

        self.addButton(label="", icon=ICON_DIR + "/shapeParent.png" ,command=ParentingFunctions.ShapeParent)

        self.addButton(label="", icon=ICON_DIR + "/shapeInstance.png" ,command=ParentingFunctions.shapeParentInstance)

        self.addButton(label="", icon=ICON_DIR + "/dupParentOnly.png", command="cmds.duplicate(parentOnly=True)")

        self.addButton(label="", icon=ICON_DIR + "/matchTransforms.png")
        transformMatchingMenu = mc.popupMenu(b=1)

        self.addMenuItem(transformMatchingMenu, "match All", command=lambda _: matchTransforms.matchAll())

        self.addMenuItem(transformMatchingMenu, "match Translation", command=lambda _: matchTransforms.matchTranslation())

        self.addMenuItem(transformMatchingMenu, "match Rotation", command=lambda _: matchTransforms.matchRotation())

        self.addMenuItem(transformMatchingMenu, "match Scale", command=lambda _: matchTransforms.matchScale())

        self.addButton(label="", icon=ICON_DIR + "/sep.png")

        self.addButton(label="", icon=ICON_DIR + "/ZeroFunctions.png")
        zeroMenu = mc.popupMenu(b=1)

        self.addMenuItem(zeroMenu, "Sam Zero", command=lambda _: ParentingFunctions.insertNodeBefore())
        self.addMenuItem(zeroMenu, "Tim Zero", command=lambda _: ParentingFunctions.TimZeroUserConfig())

        self.addButton(label="", icon=ICON_DIR + "/suffix.png" ,command = NamingFunctions.SuffixConfigurationWindow)

        self.addButton(label="", icon=ICON_DIR + "/sep.png")

        self.addButton(label="", icon=ICON_DIR + "/IkFk.png" ,command=IkFkFunctions.IKFKConfigurationInterface)

        self.addButton(label="", icon=ICON_DIR + "/simplePV.png" ,command= SimplePoleVector.createSimplePoleVector)

        self.addButton(label="", icon=ICON_DIR + "/PVLine.png" ,command= PoleVectorLineFunctions.CreatePoleVectorLine)

        self.addButton(label="", icon=ICON_DIR + "/revChain.png" ,command= ReverseFoot.createReverseChain)

        self.addButton(label="", icon=ICON_DIR + "/samStretch.png" ,command=SamStretchSetup.SamStretchSetupConfigInterface)

        self.addButton(label="", icon=ICON_DIR + "/twistJoints.png" ,command=addTwistJointsFunction.twistSetupConfigInterface)

        self.addButton(label="", icon=ICON_DIR + "/jiggleSetup.png" ,command = JiggleSetup.createJiggleSetup)

        self.addButton(label="", icon=ICON_DIR + "/sep.png")
        
        self.addButton(label="", icon=ICON_DIR + "/color.png" ,command=ColorFunctions.ColorSettingWindow)

        self.addButton(label="", icon=ICON_DIR + "/basicCtrls.png" ,command= CreateControlsFunction.CreateCircleCtrls)

        self.addButton(label="", icon=ICON_DIR + "/sep.png")

        self.addButton(label="", icon=ICON_DIR + "/mtrxZero.png" ,command=CreateMatrixOffset.iterateCreateMatrixZeroOffset)
        
        self.addButton(label="", icon=ICON_DIR + "/mtxDrvOffset.png" ,command=MatrixOffset.createMatrixDrvOffset)

        self.addButton(label="", icon=ICON_DIR + "/sep.png")

        self.addButton( label="", icon=ICON_DIR + "/multiConnect.png" ,command= MultiConnect.MultiConnectConfigurationInterface)

        #Multi Constraining
        self.addButton(label="", icon=ICON_DIR + "/multiConstraint.png")
        multiConstraining_menu = mc.popupMenu(b=1)

        ##Adding all menu items for Multi Constraining
        self.addMenuItemDivider(multiConstraining_menu, divider=True, dividerLabel="CHOOSE CONSTRAINT TYPE")

        self.addMenuItem(multiConstraining_menu, "Parent Constraint", command="from RiggingHelperTillsToolkit import ConstraintFunctions; " "ConstraintFunctions.MultiParentConstraint()")

        self.addMenuItem(multiConstraining_menu, "Orient Constraint", command="from RiggingHelperTillsToolkit import ConstraintFunctions; " "ConstraintFunctions.MultiOrientConstraint()")

        self.addMenuItem(multiConstraining_menu, "Scale Constraint", command="from RiggingHelperTillsToolkit import ConstraintFunctions; " "ConstraintFunctions.MultiScaleConstraint()")

        self.addButton( label="", icon=ICON_DIR + "/dist.png" ,command= createDistanceBetween.createDistance)

        self.addButton(label="", icon=ICON_DIR + "/sep.png")

        
        


############################ Custom Shelf End ############################



##Test Function
def Run_Test():
    print("Successful Installation")
############################