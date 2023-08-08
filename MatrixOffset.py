import maya.cmds as mc




####create an offset compose matrix when the zro compose matrix and mult matrix for the zero multiplication is selected
def createMatrixDrvOffset():
    sel = mc.ls(selection=True)


    try:
        zroName = sel[0].replace('_zro', '_drv')
    except:
        print(sel[0])

    mc.disconnectAttr(sel[0] + '.outputMatrix', sel[1] + '.matrixIn[0]')

    newMultMatrix = mc.createNode('multMatrix')

    driverMatrix = mc.createNode('composeMatrix', name= zroName)

    mc.connectAttr(newMultMatrix + '.matrixSum', sel[1] + '.matrixIn[0]')


    mc.connectAttr(driverMatrix + '.outputMatrix', newMultMatrix + '.matrixIn[0]')
    mc.connectAttr(sel[0] + '.outputMatrix', newMultMatrix + '.matrixIn[1]')
#######################