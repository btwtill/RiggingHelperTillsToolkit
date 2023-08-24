import maya.cmds as mc




def createSimplePoleVector():
    
    sel = mc.ls(selection=True)
    
    if len(sel) == 2:
        
        ik_handle = sel[0]
        pv_ctrl = sel[1]
    
        start_joint = mc.ikHandle(ik_handle, query=True, startJoint=True)
        
        mid_joint = mc.listRelatives(start_joint, children=True, type='joint')[0]
        
        mc.delete(mc.pointConstraint(start_joint, ik_handle, pv_ctrl))
        
        mc.delete(mc.aimConstraint(mid_joint, pv_ctrl, aim=[0,0,-1], u= [-1, 0, 0], wuo=start_joint, wut='object'))
        
        pv_pos = mc.xform(pv_ctrl, q=True, ws=True, t=True)
        mid_pos = mc.xform(mid_joint, q=True, ws=True, t=True)
        
        pv_dist = (pv_pos[0] - mid_pos[0], pv_pos[1] - mid_pos[1], pv_pos[2] - mid_pos[2])
        
        mc.xform(pv_ctrl, t=(mid_pos[0] - pv_dist[0] * 1.2, mid_pos[1] - pv_dist[1] * 1.2, mid_pos[2] - pv_dist[2]* 1.2))
        
        mc.poleVectorConstraint(pv_ctrl, ik_handle)

        pv_off = mc.duplicate(pv_ctrl, po=True, name=pv_ctrl + "_grp")
        mc.parent(pv_ctrl, pv_off)

    else:
        print("Please Select IF Hanlde and then the PV Ctrl")
    
    return True