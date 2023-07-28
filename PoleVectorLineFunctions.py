import maya.cmds as mc


def CreatePoleVectorLine():
    try:
            
        sel = mc.ls(selection=True)

        qshape = mc.curve(p=[(0,0,0), (0,0,0)], d=1)


        qshape = mc.rename(qshape, sel[0] + '_q')
        mc.select(qshape)

        selectionShape = mc.pickWalk(direction="Down")


        mc.parent(selectionShape, sel[0], shape=True, relative=True)

        multmatrix = mc.createNode('multMatrix')
        decomposeMatrix = mc.createNode('decomposeMatrix')


        mc.connectAttr(multmatrix + '.matrixSum', decomposeMatrix + '.inputMatrix')

        mc.connectAttr(sel[1] + '.worldMatrix', multmatrix + '.matrixIn[0]')
        mc.connectAttr(sel[0] + '.worldInverseMatrix[0]', multmatrix + '.matrixIn[1]')


        mc.connectAttr(decomposeMatrix + '.outputTranslateX', selectionShape[0] + '.controlPoints[0].xValue')
        mc.connectAttr(decomposeMatrix + '.outputTranslateY', selectionShape[0] + '.controlPoints[0].yValue')
        mc.connectAttr(decomposeMatrix + '.outputTranslateZ', selectionShape[0] + '.controlPoints[0].zValue')

        mc.delete(qshape)
    except:
        print("time to investigate!!")





# sel = cmds.ls(selection=True)

# cmds.select(clear=True)

# jointList = []
# ctrlList = []
# for i in sel:
#     translation = cmds.xform(i, q=True, ws=True, translation=True)
#     rotation = cmds.xform(i, q=True, ws=True, rotation=True)
#     print(translation, rotation)
#     newJoint = cmds.joint(name=i, orientation=rotation, position=translation)
#     jointList.append(newJoint)
#     ctrl = cmds.circle(name=newJoint + '_ctrl')
#     cmds.setAttr(ctrl[0] + '.translate', *translation)
#     cmds.setAttr(ctrl[0] + '.rotate', *rotation)
#     ctrlList.append(ctrl)
#     cmds.select(clear=True)
    
# jointList = list(reversed(jointList))
# ctrlList = list(reversed(ctrlList))

# for i in range(len(jointList)):
#     if i != (len(jointList) - 1):
#         print(i)
#         cmds.parent(jointList[i], jointList[i + 1])
#         cmds.parent(ctrlList[i], ctrlList[i+1])
        
        
#     else:
#         print("lastIndex")
        


# ##add offset and Zro CTRls
# cmds.circle()

