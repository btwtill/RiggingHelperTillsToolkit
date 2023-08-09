from RiggingHelperTillsToolkit import generalFunctions
from PySide2 import QtWidgets, QtGui, QtCore
import maya.cmds as cmds


class TextfieldButtonGroup(QtWidgets.QWidget):

    def __init__(self, group_name, parent=None):
        super(TextfieldButtonGroup, self).__init__(parent)
        self.group_name = group_name
        self.initUI()
        
    def initUI(self):

        #set Widget Layout
        layout = QtWidgets.QVBoxLayout()

        #create Label and add it to the widget
        group_label = QtWidgets.QLabel(self.group_name, self)
        layout.addWidget(group_label)

        # #create first textfield and add it to the widget
        # self.text_field = QtWidgets.QLineEdit(self)
        # layout.addWidget(self.text_field)

        #create the button and connect the function to update the label with the button as well as adding the button to the widget
        update_button = QtWidgets.QPushButton("set Pos", self)
        layout.addWidget(update_button)
        update_button.clicked.connect(self.updateLabel)

        #create label displaing the selected joint
        self.label = QtWidgets.QLabel("Joint Selection", self)
        layout.addWidget(self.label)

        self.setLayout(layout)


#Function to update the label in the textfield
    def updateLabel(self):
        new_text = cmds.ls(selection=True)
        self.label.setText(new_text[0])

        rgb_color = [0.01, 0.01, 0.01]

        label_palette = self.label.palette()
        new_color = QtGui.QColor(*rgb_color)

        label_palette.setColor(QtGui.QPalette.Window, new_color)
        self.label.setAutoFillBackground(True)
        self.label.setPalette(label_palette)



class StretchSetup(QtWidgets.QWidget):
    def __init__(self):
        super(StretchSetup, self).__init__()

        self.groups = {}  # Dictionary to store TextfieldButtonGroup instances
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Sams Stretch Setup")
        self.setGeometry(50, 50, 200, 200)

        main_layout = QtWidgets.QVBoxLayout()

        upperJoint = TextfieldButtonGroup("Upper Joint", self)
        self.groups["Upper Joint"] = upperJoint  # Store instance in the dictionary
        main_layout.addWidget(upperJoint)

        midJoint = TextfieldButtonGroup("Mid Joint", self)
        self.groups["Mid Joint"] = midJoint  # Store instance in the dictionary
        main_layout.addWidget(midJoint)

        lowerJoint = TextfieldButtonGroup("Lower Joint", self)
        self.groups["Lower Joint"] = lowerJoint  # Store instance in the dictionary
        main_layout.addWidget(lowerJoint)

        selAnchor = TextfieldButtonGroup("Anchor", self)
        self.groups["Anchor"] = selAnchor  # Store instance in the dictionary
        main_layout.addWidget(selAnchor)

        selPoleVector = TextfieldButtonGroup("Pole Vector", self)
        self.groups["Pole Vector"] = selPoleVector  # Store instance in the dictionary
        main_layout.addWidget(selPoleVector)

        selEndJoint = TextfieldButtonGroup("End Joint", self)
        self.groups["End Joint"] = selEndJoint  # Store instance in the dictionary
        main_layout.addWidget(selEndJoint)

        build_stretch_setup_button = QtWidgets.QPushButton("Build Stretch Setup", self)
        build_stretch_setup_button.clicked.connect(self.BuildStretchSetup)
        main_layout.addWidget(build_stretch_setup_button)

        self.setLayout(main_layout)
        
    def getLabelText(self, group_name):
        if group_name in self.groups:
            return self.groups[group_name].label.text()
        
    def getCharacterSideNamingConvention(self, context):
        leftFilterString = ["L_", "l_", "lf_", "LF_", "Left_", "left_"]
        rightFilterStrings = ["R_", "r_", "ri_", "RI_", "Right", "right"]

        rightEntrys = generalFunctions.filter_strings(context, rightFilterStrings)
        leftEntrys = generalFunctions.filter_strings(context, leftFilterString)

        if rightEntrys:
            return "_r_"
        elif leftEntrys:
            return "_l_"
        else:
            return "NOT Defined"
        
    def createDefaultChain(self, _targetChain):
        return generalFunctions.removeOneAndPrefixName(generalFunctions.duplicateSelection(_targetChain), "def_")


    def setupConnections(self, _End_ctrl, _PoleVector_ctrl, _anchor, _side, _DefaultIKChain, _stretchAttributes):

        #Anchor to Pole Vector
        upperLength = cmds.rename(cmds.createNode('distanceBetween'), _side + "upper_lenght")

        cmds.connectAttr(_anchor + ".worldMatrix[0]", upperLength + ".inMatrix1")
        cmds.connectAttr(_PoleVector_ctrl + ".worldMatrix[0]", upperLength + ".inMatrix2")

        #Pole Vector to End

        lowerLength = cmds.rename(cmds.createNode('distanceBetween'), _side + "lower_lenght")

        cmds.connectAttr(_PoleVector_ctrl + ".worldMatrix[0]", lowerLength + ".inMatrix1")
        cmds.connectAttr(_End_ctrl + ".worldMatrix[0]", lowerLength + ".inMatrix2")

        #ChainLenght
        activeLenght = cmds.rename(cmds.createNode('distanceBetween'), _side + "lenght")

        cmds.connectAttr(_anchor + ".worldMatrix[0]", activeLenght + ".inMatrix1")
        cmds.connectAttr(_End_ctrl + ".worldMatrix[0]", activeLenght + ".inMatrix2")

        #Default Distance Calculation

        defaultUpperLenght = cmds.rename(cmds.createNode('distanceBetween'), _side + "default_upper_lenght")

        cmds.connectAttr(_DefaultIKChain[0] + '.worldMatrix[0]', defaultUpperLenght + ".inMatrix1")
        cmds.connectAttr(_DefaultIKChain[1] + '.worldMatrix[0]', defaultUpperLenght + ".inMatrix2")

        defaultLowerLenght = cmds.rename(cmds.createNode('distanceBetween'), _side + "default_lower_lenght")

        cmds.connectAttr(_DefaultIKChain[1] + '.worldMatrix[0]', defaultLowerLenght + ".inMatrix1")
        cmds.connectAttr(_DefaultIKChain[2] + '.worldMatrix[0]', defaultLowerLenght + ".inMatrix2")

        defaultLenght = cmds.rename(cmds.createNode('distanceBetween'), _side + "default_lenght")

        cmds.connectAttr(_DefaultIKChain[0] + '.worldMatrix[0]', defaultLenght + ".inMatrix1")
        cmds.connectAttr(_DefaultIKChain[2] + '.worldMatrix[0]', defaultLenght + ".inMatrix2")

        #calculate stretch value with active and default length values
        stretchValue = cmds.rename(cmds.createNode('floatMath'), _side + "stretch_value")

        cmds.connectAttr(activeLenght + ".distance", stretchValue + ".floatA")
        cmds.connectAttr(defaultLenght + ".distance", stretchValue + ".floatB")

        #implement max stretch attribute with clamp node
        maxStretch = cmds.rename(cmds.createNode('clamp'), _side + "Max_Stretch")

        cmds.setAttr(maxStretch + ".minR", 1)

        cmds.connectAttr(stretchValue + ".outFloat", maxStretch + ".inputR")
        cmds.connectAttr(_End_ctrl + _stretchAttributes[4], maxStretch + ".maxR")

        #implement do Stretch attribute with blend two attributes node

        #Multiply default upper and lower lenght with multiply value

        #Implement nudge multiplication with nudge attribute

        #add the nudge value on

        #implement knee pin with two blendtwoAttr nodes

        #if right side add a multiplication with -1 to invert the number

        #connect to the actual ik joints

    def addStretchAttributes(self, targetObject, attributes):
        cmds.addAttr(targetObject, longName=attributes[0], attributeType="enum", keyable=True, enumName='*****')
        cmds.addAttr(targetObject, longName=attributes[1], attributeType="float", keyable=True, minValue=0, maxValue=1)
        cmds.addAttr(targetObject, longName=attributes[2], attributeType="float", keyable=True, minValue=0, maxValue=1)
        cmds.addAttr(targetObject, longName=attributes[3], attributeType="float", keyable=True)
        cmds.addAttr(targetObject, longName=attributes[4], attributeType="float", keyable=True, minValue=0, defaultValue=2)

    def BuildStretchSetup(self):

        stretchAttributes = ["Stretch_Ctrls", "Do_Stretch", "Pin", "Nudge", "Max_Stretch"]
        selectionContext = []

        #extrackt all the positions set by the user
        for group_name in self.groups:
            selectionContext.append(self.getLabelText(group_name))

        #build components out of the user selection for further use in the script
        IKChain = [selectionContext[0], selectionContext[1], selectionContext[2]]
        anchor = selectionContext[3]
        poleVector = selectionContext[4]
        endJoint = selectionContext[5]
        side = self.getCharacterSideNamingConvention(IKChain)

        #create default lenth chain
        defualtChain = self.createDefaultChain(IKChain)
        generalFunctions.reparenting(defualtChain)

        #Add the Stretch Attributes to the corresponding end ctrl
        self.addStretchAttributes(endJoint, stretchAttributes)

        #create the distnace calculations and connect the attributes
        self.setupConnections(endJoint, poleVector, anchor, side, defualtChain, stretchAttributes)

        




###Display the actual window

StretchWindow = StretchSetup()

def show_ui():
    StretchWindow.show()

show_ui()