import maya.cmds as mc

def _null(*args):
    pass


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






class customShelf(_shelf):
    def build(self):
        self.addButton(label="Test_Run", command=Run_Test)
        self.addButton(label="ShapeParent", command=ShapeParent)
        self.addButton(label="SamZero", command=insertNodeBefore)







def ShapeParent(*args):
    selection = mc.ls(selection=True)
    PosOffset = True

    if(selection):
        mc.parent(selection[0], selection[1], shape=True, relative=PosOffset)


def Run_Test():
    print("Successful Installation")



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