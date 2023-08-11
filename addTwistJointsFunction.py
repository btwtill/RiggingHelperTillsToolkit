import maya.mc as mc


def twistSetupConfigInterface():
    configWindow = mc.window(title="TwistJoints", iconName="TwistJoints", widthHeight=(200, 55), sizeable=True)

    mc.rowColumnLayout( adjustableColumn=True )

    mc.text(label="Select number of Twist Joints")

    global label
    label = mc.text(label="0")

    slider = mc.floatSlider(min=0, max=30, value=0, step=1, changeCommand=update_label)

    mc.button(label="Create Twist Joints", command=lambda _:createTwistSetup(mc.floatSlider(slider, query=True, value=True)))

    mc.showWindow(configWindow)


def update_label(value):
    mc.text(label, edit=True, label=str(int(value)))

def createTwistSetup(_numberOfJoints):
    numberOfJoints = int(_numberOfJoints)
    print(numberOfJoints)

    sel = mc.ls(selection=True)

    p1 = sel[0]
    p2 = sel[1]

    name = "".join(p1)

    twistJoints = createJoints(numberOfJoints, name)

    weights01 , weights02 = getWeights(numberOfJoints)

    createTwistJointPointConstraints(twistJoints, p1, p2, weights01, weights02)

def createJoints(_numberOfJoints, _name):
    twistJoints = []
    for i in range(_numberOfJoints):
        mc.select(clear=True)
        newJoint = mc.rename(mc.joint(), _name + "_Twist")
        twistJoints.append(newJoint)
    return twistJoints
        

def createTwistJointPointConstraints(_twistJoints, _p1, _p2, _weights01, _weights02):
    for i in range(len(_twistJoints)):
        pointConstraint = mc.pointConstraint(_p1, _p2, _twistJoints[i])

        mc.setAttr(pointConstraint[0] + "." + _p1 + "W0", _weights02[i])
        mc.setAttr(pointConstraint[0] + "." + _p2 + "W1", _weights01[i])


def getWeights(_numberOfJoints):

    _numberOfJoints = 5

    weights01 = []
    weights02 = []

    for i in range(_numberOfJoints - 1):
        print(i + 1)
        print(_numberOfJoints - 1)
        weight = (i + 1) / (_numberOfJoints - 1)
        print(round(weight, 2))
        weights01.append(round(weight, 2))


    for i in range(len(weights01)):
        if weights01[i] == 1:
            weights01[i] = 0.95
        
    weights01.insert(0, 0.05)

    for i in weights01:
        weights02.append(round(abs(i - 1),2))
        

    return weights01, weights02
    



twistSetupConfigInterface()