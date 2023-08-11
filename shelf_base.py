import maya.cmds as mc

from RiggingHelperTillsToolkit import IkFkFunctions, ParentingFunctions, ColorFunctions, NamingFunctions, PoleVectorLineFunctions, ReverseFoot, CreateControlsFunction, MatrixOffset, MultiConnect, SamStretchSetup, addTwistJointsFunction


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
        self.addButton(label="Test_Run", command=Run_Test)


        self.addButton(label="ShapeParent", command=ParentingFunctions.ShapeParent)
        self.addButton(label="ShapeInstance", command=ParentingFunctions.shapeParentInstance)
        self.addButton(label="SamZero", command=ParentingFunctions.insertNodeBefore)


        self.addButton(label="Suffix Selected", command = NamingFunctions.SuffixConfigurationWindow)


        self.addButton(label="IKFKSwitch", command=IkFkFunctions.IKFKConfigurationInterface)

        
        self.addButton(label="ColorAnimationCtrl", command=ColorFunctions.ColorSettingWindow)

        
        self.addButton(label="PoleVectorLine", command= PoleVectorLineFunctions.CreatePoleVectorLine)

        self.addButton(label="ReverseChain", command= ReverseFoot.createReverseChain)

        self.addButton(label="CircleCtrls", command= CreateControlsFunction.CreateCircleCtrls)

        self.addButton(label="MatrixDrvOffset", command=MatrixOffset.createMatrixDrvOffset)

        self.addButton( label="MultiConnect", command= MultiConnect.MultiConnectConfigurationInterface)

        self.addButton(label="SamStretchSetup", command=SamStretchSetup.SamStretchSetupConfigInterface)

        self.addButton(label="TwistJoints", command=addTwistJointsFunction.twistSetupConfigInterface)


        #Multi Constraining
        self.addButton(label="MultiConstraint")
        multiConstraining_menu = mc.popupMenu(b=1)

        ##Adding all menu items for Multi Constraining
        self.addMenuItemDivider(multiConstraining_menu, divider=True, dividerLabel="CHOOSE CONSTRAINT TYPE")

        self.addMenuItem(multiConstraining_menu, "Parent Constraint", command="from RiggingHelperTillsToolkit import ConstraintFunctions; " "ConstraintFunctions.MultiParentConstraint()")

        self.addMenuItem(multiConstraining_menu, "Orient Constraint", command="from RiggingHelperTillsToolkit import ConstraintFunctions; " "ConstraintFunctions.MultiOrientConstraint()")

        self.addMenuItem(multiConstraining_menu, "Scale Constraint", command="from RiggingHelperTillsToolkit import ConstraintFunctions; " "ConstraintFunctions.MultiScaleConstraint()")
        


############################ Custom Shelf End ############################



##Test Function
def Run_Test():
    print("Successful Installation")
############################