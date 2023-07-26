import maya.cmds as mc




#Functino to Parent Constaraint Multiple Objects with each Other
def MultiParentConstraint():
    sel = mc.ls(selection=True)
    try:
        ctrlListTarget = "_ctrl"
        jointListTarget = "_jnt"

        filteredCtrlList = [s for s in sel if ctrlListTarget in s]
        filteredJntList = [s for s in sel if jointListTarget in s]

        if len(filteredCtrlList) == len(filteredJntList):

            for i in range(len(filteredCtrlList)):
                mc.parentConstraint(filteredCtrlList[i], filteredJntList[i])



    except:
        print("Nope!!")



#Functino to Orient Constaraint Multiple Objects with each Other
def MultiOrientConstraint():
    sel = mc.ls(selection=True)
    try:
        ctrlListTarget = "_ctrl"
        jointListTarget = "_jnt"

        filteredCtrlList = [s for s in sel if ctrlListTarget in s]
        filteredJntList = [s for s in sel if jointListTarget in s]

        if len(filteredCtrlList) == len(filteredJntList):

            for i in range(len(filteredCtrlList)):
                mc.orientConstraint(filteredCtrlList[i], filteredJntList[i])



    except:
        print("Nope!!")


#Functino to Scale Constaraint Multiple Objects with each Other
def MultiScaleConstraint():
    sel = mc.ls(selection=True)
    try:
        ctrlListTarget = "_ctrl"
        jointListTarget = "_jn"

        filteredCtrlList = [s for s in sel if ctrlListTarget in s]
        filteredJntList = [s for s in sel if jointListTarget in s]

        if len(filteredCtrlList) == len(filteredJntList):

            for i in range(len(filteredCtrlList)):
                mc.scaleConstraint(filteredCtrlList[i], filteredJntList[i])



    except:
        print("Nope!!")

