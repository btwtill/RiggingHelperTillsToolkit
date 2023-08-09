from RiggingHelperTillsToolkit import generalFunctions


sel = cmds.ls(selection=True)


def seperateSelectionListToComponents(selectionList):
    IK_Chain_Component = []
    Wrist_Ctrl_Component = ""
    PoleVector_Component = ""
    Anchor_Component = ""

    side_naming = ""



    for i in selectionList:
        if "IK" in i and "ctrl" not in i:
            IK_Chain_Component.append(i)
    
    for i in selectionList:
        if "Wrist" in i:
            Wrist_Ctrl_Component = i
            break
        else:
            Wrist_Ctrl_Component = "not Defined, what the naming convention!"

    for i in selectionList:
        if "PoleVector" in i or "poleVector" in i or "polevector" in i:
            PoleVector_Component = i
            break
        else:
            PoleVector_Component = "not Defined, what the naming convention!"
    for i in selectionList:
        if "ANCHOR" in i or "anchor" in i:
            Anchor_Component = i
            break
        else:
            Anchor_Component= "not Defined, what the naming convention!"

    for i in selectionList:
        if "L_" in i or "l_" in i or "lf_" in i or "LF_" in i:
            side_naming = "_l_"
        elif "R_" in i or "r_" in i or "ri_" in i or "RI_" in i:
            side_naming = "_r_"

    return IK_Chain_Component, Wrist_Ctrl_Component, PoleVector_Component, Anchor_Component, side_naming






Ik_Chain, Wrist_ctrl, PoleVector_ctrl, anchor, side_naming = seperateSelectionListToComponents(sel)

defaultIKChain = generalFunctions.removeOneAndPrefixName(generalFunctions.duplicateSelection(Ik_Chain), "def_")

generalFunctions.reparenting(defaultIKChain)