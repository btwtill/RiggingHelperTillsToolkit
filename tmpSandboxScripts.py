# defin the mid joint q
mid_joint = "joint9"

mid_joint_pos = cmds.xform(mid_joint, q=True, ws=True, t=True)
# define array with target joints
target_joints = cmds.ls(selection=True)

#for all target joints

for i in target_joints:
    
    # define locator pos and target joint pos
    target_pos = cmds.xform(i, q=True, ws=True, t=True)
    
    # create locator and match to mid joint
    new_locator = cmds.spaceLocator(name=mid_joint + "_" + i + "_" + "pos")
    
    cmds.xform(new_locator, t=mid_joint_pos)
    
    # create aimconstraint between locator and target joint
    cmds.delete(cmds.aimConstraint(i, new_locator, aim=[1, 0, 0], u=[0, 1, 0], wut="scene"))
    
    # calc distance
    dist = (mid_joint_pos[0] - target_pos[0], mid_joint_pos[1] - target_pos[1], mid_joint_pos[2] - target_pos[2])
    
    # move joint by distance 
    
    cmds.xform(new_locator, t=(mid_joint_pos[0] - dist[0], mid_joint_pos[1] - dist[1], mid_joint_pos[2] - dist[2]))
    
    newPos = cmds.xform(new_locator, q=True, ws=True, t=True)
    
    cmds.parent(cmds.rename(cmds.joint(p=newPos), new_locator[0] + "_jnt"), world=True)
    
    cmds.delete(new_locator)
