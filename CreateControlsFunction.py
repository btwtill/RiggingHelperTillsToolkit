import maya.cmds as mc


def CreateCircleCtrls():

    sel = mc.ls(selection=True)


    ctrlList = []
    for i in sel:
        translation = mc.xform(i, q=True, ws=True, t=True)
        rotation = mc.xform(i, q=True, ws=True, rotation=True)
        
        newCtrl = mc.circle(name=i)
        
        mc.setAttr(newCtrl[0]+'.translate', *translation)
        mc.setAttr(newCtrl[0] + '.rotate', *rotation)
        ctrlList.append(newCtrl)
        
    ctrlList = list(reversed(ctrlList))
    for i in range(len(ctrlList)):
        if i != (len(ctrlList) - 1):
            mc.parent(ctrlList[i], ctrlList[i + 1])