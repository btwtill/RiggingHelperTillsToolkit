import maya.cmds as mc



def createReverseChain():
    sel = mc.ls(selection=True)

    mc.select(clear=True)

    jointList = []
    ctrlList = []

    for i in sel:
        translation = mc.xform(i, q=True, ws=True, translation=True)
        rotation = mc.xform(i, q=True, ws=True, rotation=True)
        
        newJoint = mc.joint(name=i, orientation=rotation, position=translation)
        jointList.append(newJoint)
        
        if i == "Heel":
            exractrl = mc.circle(name=newJoint + '_swivel_ctrl')
            mc.setAttr(exractrl[0] + '.translate', *translation)
            mc.setAttr(exractrl[0] + '.rotate', *rotation)
            ctrlList.append(exractrl)
        if i == "Tip":
            exractrl = mc.circle(name=newJoint + '_swivel_ctrl')
            mc.setAttr(exractrl[0] + '.translate', *translation)
            mc.setAttr(exractrl[0] + '.rotate', *rotation)
            ctrlList.append(exractrl)
            
        ctrl = mc.circle(name=newJoint + '_ctrl')
        mc.setAttr(ctrl[0] + '.translate', *translation)
        mc.setAttr(ctrl[0] + '.rotate', *rotation)
        ctrlList.append(ctrl)
        
        mc.select(clear=True)
        
        
    jointList = list(reversed(jointList))
    ctrlList = list(reversed(ctrlList))


    def hirarchyReparenting(_targetList):
        for i in range(len(_targetList)):
            if i != (len(_targetList) - 1):
                mc.parent(_targetList[i], _targetList[i + 1])
            else:
                pass

    hirarchyReparenting(jointList)
    hirarchyReparenting(ctrlList)

