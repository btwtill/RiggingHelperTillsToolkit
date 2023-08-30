import maya.cmds as mc




#Functino to Parent Constaraint Multiple Objects with each Other
def MultiParentConstraintConfig():
    configWindow = mc.window(title="ParentConstraintConfig", sizeable=True, iconName="MultiParent", widthHeight=(200, 55))
    
    mc.rowColumnLayout(adjustableColumn=True)

    mc.text(label="Search for master suffix")

    firstItemSufffix = mc.textField()

    mc.text(label="Search for target suffix")

    seconItemSufffix = mc.textField()

    mc.button(label="Parent", command= lambda _: MultiParentConstraint(mc.textField(firstItemSufffix, query=True, text=True), mc.textField(seconItemSufffix, query=True, text=True)))

    mc.showWindow(configWindow)

def MultiParentConstraint(_firstSuffix, _secondSuffix):
    sel = mc.ls(selection=True)
    try:
        constrainingList = _firstSuffix
        targetList = _secondSuffix

        filteredFirstList = [s for s in sel if constrainingList in s]
        filteredSecondList = [s for s in sel if targetList in s]

        if len(filteredFirstList) == len(filteredSecondList):

            for i in range(len(filteredFirstList)):
                mc.parentConstraint(filteredFirstList[i], filteredSecondList[i])



    except:
        print("Nope!!")


def MultiOrientConstraintConfig():
    configWindow = mc.window(title="OrientConstraintConfig", sizeable=True, iconName="MultiOrient", widthHeight=(200, 55))
    
    mc.rowColumnLayout(adjustableColumn=True)

    mc.text(label="Search for master suffix")

    firstItemSufffix = mc.textField()

    mc.text(label="Search for target suffix")

    seconItemSufffix = mc.textField()

    mc.button(label="Orient", command= lambda _: MultiOrientConstraint(mc.textField(firstItemSufffix, query=True, text=True), mc.textField(seconItemSufffix, query=True, text=True)))

    mc.showWindow(configWindow)


#Functino to Orient Constaraint Multiple Objects with each Other
def MultiOrientConstraint(_firstSuffix, _secondSuffix):
    sel = mc.ls(selection=True)
    try:
        constrainingList = _firstSuffix
        targetList = _secondSuffix

        filteredFirstList = [s for s in sel if constrainingList in s]
        filteredSecondList = [s for s in sel if targetList in s]

        if len(filteredFirstList) == len(filteredSecondList):

            for i in range(len(filteredFirstList)):
                mc.orientConstraint(filteredFirstList[i], filteredSecondList[i])



    except:
        print("Nope!!")


def MultiScaleConstraintConfig():
    configWindow = mc.window(title="ScaleConstraintConfig", sizeable=True, iconName="MultiScale", widthHeight=(200, 55))
    
    mc.rowColumnLayout(adjustableColumn=True)

    mc.text(label="Search for master suffix")

    firstItemSufffix = mc.textField()

    mc.text(label="Search for target suffix")

    seconItemSufffix = mc.textField()

    mc.button(label="Scale", command= lambda _: MultiScaleConstraint(mc.textField(firstItemSufffix, query=True, text=True), mc.textField(seconItemSufffix, query=True, text=True)))

    mc.showWindow(configWindow)


#Functino to Scale Constaraint Multiple Objects with each Other
def MultiScaleConstraint(_firstSuffix, _secondSuffix):
    sel = mc.ls(selection=True)
    try:
        constrainingList = _firstSuffix
        targetList = _secondSuffix

        filteredFirstList = [s for s in sel if constrainingList in s]
        filteredSecondList = [s for s in sel if targetList in s]

        if len(filteredFirstList) == len(filteredSecondList):

            for i in range(len(filteredFirstList)):
                mc.scaleConstraint(filteredFirstList[i], filteredSecondList[i])



    except:
        print("Nope!!")

