import maya.cmds as mc


def CreatePoleVectorLine():
    try:
            
        sel = mc.ls(selection=True)

        qshape = mc.curve(p=[(0,0,0), (0,0,0)])


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
