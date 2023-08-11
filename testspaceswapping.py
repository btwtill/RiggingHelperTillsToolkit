import maya.cmds as mc


def SpaceSwapConfig():
    configWindow = mc.window(title="SpaceSwapSetup", iconName="SpaceSwap", sizeable=True)
    
    mc.rowColumnLayout( adjustableColumn=True )
    
    cmds.text( label='Contraint Object', font = "boldLabelFont", height=30, align="left")
    
    contraintObject = buildUserInputGrp("Select Contraint Object", "No Contraint Object Selected", 20)
    
    global label
    label = mc.text(label="0")
    
    mc.text(label="Choose the amout of targets you need")
    slider = mc.floatSlider(min=0, max=4, value=0, step=1, changeCommand=update_slider_label)
    
    addTargetsButton = mc.button(label="Add Targets", command=lambda _: AddTargetInputGrps(mc.floatSlider(slider, query=True, value=True)))
    
    mc.button(label="Build Space Switch", command=lambda _: BuildSpaceSwitch(targetList))
    
    mc.showWindow(configWindow)


def buildUserInputGrp(buttonLabel, displayLabelText, displayLabelHeight):
    mc.text(label="", height=40)
    mc.text(label="", height=10, backgroundColor=[0.2,0.2,0.2])
    mc.button(label=buttonLabel, height=40, command=lambda _: updateLabel(labelname, getFirstUserSelection()))
    labelname = mc.text(label=displayLabelText, height=displayLabelHeight, backgroundColor=[1.0, 0.0, 0.0])
    mc.text(label="", height=40)
 
    return labelname
    
def BuildSpaceSwitch(input):
    print(input)

def AddTargetInputGrps(numberOfTargets):
    targetList = []
    for i in range(int(numberOfTargets)):
        newTarget = buildUserInputGrp("Select Target Space Object", "No Target Space Selected", 20)
        targetList.append(newTarget)
    return targetList

def getFirstUserSelection():
    sel = mc.ls(selection=True)
    return sel[0]
    
def update_slider_label(value):
    mc.text(label, edit=True, label=str(int(value)))


def updateLabel(_label, _newLabelText):
    rgbColor = [0.2, 0.2, 0.2]
    cmds.text(_label, edit=True, label=_newLabelText, backgroundColor=rgbColor)


SpaceSwapConfig()

