import maya.cmds as mc


############## Color Options ##############

def ColorSettingWindow():

    #initilizing the window to pick the color
    configurationWindow = mc.window(title="Animation Ctrl Color", iconName="CTRl Color", widthHeight=(200, 200), sizeable=True)

    #set Window Layout
    mc.rowColumnLayout(adjustableColumn=True)

    #User Color Input
    color_widget_input = mc.colorInputWidgetGrp( label='Color', rgb=(1, 0, 0) )

    doRecolorOutliner = mc.checkBox(label="Recolor Zero Node in Outliner", value=True)

    #button to hand rgb value to function that executes the recoloring
    getColorButton = mc.button(label="Set Color", command=lambda _: setCtrlShapeColorAttribute(mc.colorInputWidgetGrp(color_widget_input, query=True, rgb=True), mc.checkBox(doRecolorOutliner, query=True, value=True)))

    #Show the Configuration Window
    mc.showWindow(configurationWindow)






def setCtrlShapeColorAttribute(_color, _recolorOutliner):
    colorRGB = _color

    sel = mc.ls(sl = 1)

    for node in sel:
        #get shape Nodes
        shapes = mc.listRelatives(node, s = 1)
        if shapes:
            for shp in shapes:
                try:
                    ## Add Color and Node Connection
                    mc.setAttr(shp + '.overrideEnabled', 1)
                    mc.setAttr(shp + '.overrideRGBColors', 1)
                    mc.setAttr(shp + '.overrideColorR', colorRGB[0])
                    mc.setAttr(shp + '.overrideColorG', colorRGB[1])
                    mc.setAttr(shp + '.overrideColorB', colorRGB[2])

                    if _recolorOutliner:
                        
                        parentNode = mc.listRelatives(node, parent=True)
                        parentNodeName = "".join(parentNode)
                        
                        mc.setAttr(parentNodeName + ".useOutlinerColor", True)
                        mc.setAttr(parentNodeName + ".outlinerColorR", colorRGB[0])
                        mc.setAttr(parentNodeName + ".outlinerColorG", colorRGB[1])
                        mc.setAttr(parentNodeName + ".outlinerColorB", colorRGB[2])
                        
                except:
                    pass

        # try:
        #     ## Add Color and Node Connection
        #     mc.setAttr(node + '.overrideEnabled', 1)
        #     mc.setAttr(node + '.overrideRGBColors', 1)
        #     mc.setAttr(node + '.overrideColorR', colorRGB[0])
        #     mc.setAttr(node + '.overrideColorG', colorRGB[1])
        #     mc.setAttr(node + '.overrideColorB', colorRGB[2])
        # except:
        #     pass

##########################################