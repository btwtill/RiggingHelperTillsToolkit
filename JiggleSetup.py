import maya.cmds as mc

#Function to create fake muscle jiggle setup
def createJiggleSetup():

    #get user Joint Selection
    sel = mc.ls(selection=True)

    #get the parent of the user selection 
    parentJoint = mc.pickWalk(direction="Up")

    #create the locatior structure, zro and pos
    zro_loc = mc.spaceLocator(name=sel[0] + "_loc_zro")
    pos_loc = mc.spaceLocator(name=sel[0] + "_loc_pos")

    #get the worldspace translation and rotation of the selected joint
    jointTranslation = mc.xform(sel[0], query=True, ws=True, translation=True)
    jointRotation = mc.xform(sel[0], query=True, ws=True, rotation=True)

    #set the locators translation and rotation to the same as the joint
    mc.xform(zro_loc, translation=jointTranslation)
    mc.xform(zro_loc, rotation=jointRotation)

    mc.xform(pos_loc, translation=jointTranslation)
    mc.xform(pos_loc, rotation=jointRotation)

    #parent the pos locator to the zro locator and the zro locator to the parent joint
    mc.parent(pos_loc, zro_loc)
    mc.parent(zro_loc, parentJoint)

    #create a locator that the joint will follow later
    follow_loc = mc.spaceLocator(name=sel[0] + "_loc_follow")

    #create the particle used to sim the jiggle
    newParticle = mc.particle(p=jointTranslation)

    #set the particles goal
    mc.goal(newParticle, g=pos_loc)

    #connect the worldspace position of the particle to the follow locator pos
    mc.connectAttr(newParticle[0] + ".worldCentroidX", follow_loc[0] + ".translateX")
    mc.connectAttr(newParticle[0] + ".worldCentroidY", follow_loc[0] + ".translateY")
    mc.connectAttr(newParticle[0] + ".worldCentroidZ", follow_loc[0] + ".translateZ")

    #constraint the joint between the position locator and follow locator
    mc.pointConstraint(pos_loc, follow_loc, sel[0])