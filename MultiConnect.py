import maya.cmds as mc





####Execute the Attribute Connections
def ConnectOneToNNodes(_outputNodeAttribute, _inputNodeAttribute, _outputNode, _inputNodes, _targetList):

    #get the string for the output Attribute on the output Node
    outputName = _outputNode + "." + _outputNodeAttribute
    
    #loop over the selected Input nodes and connect the selected output to the input sockets
    for i in _targetList:
        mc.connectAttr(outputName, i + "." + _inputNodeAttribute)



#Configuration Interface to let the user decide what Output Attribute should be used to connect to all the selected Input Nodes
def MultiConnectConfigurationInterface():  

    #get selection
    sel = mc.ls(selection=True)


    #seperate out the output node and input nodes into different lists
    firstElementAttributes = mc.listAttr(sel[0])
    secondElementAttribtues = mc.listAttr(sel[1])

    #firstListFirstTargetSring = "Translate"
    #firstListSecondTargetString= "Rotate"
    #firstListThirdTargetString = "Scale"

    #firstElementAttributes = [s for s in firstElementAttributes if firstListFirstTargetSring in s or firstListSecondTargetString in s or firstListThirdTargetString in s ]

    #filter the attribute list
    secondListFirstTargetSring = "Translate"
    secondListSecondTargetString= "Rotate"
    secondListThirdTargetString = "Scale"

    secondElementAttribtues = [s for s in secondElementAttribtues if secondListFirstTargetSring in s or secondListSecondTargetString in s or secondListThirdTargetString in s ]

    #safe the output Node into a seperate Variable
    OutputNode = sel.pop(0)
    InputNodes = sel[0]


    #basic Window creation
    configWindow = mc.window(title="MultiConnector", iconName='1xN', widthHeight=(200, 55), sizeable=True)

    #Window Layout
    mc.rowColumnLayout( adjustableColumn=True)

    #create the Options menues and store them in a variable
    OutputNodeOptionMenu = mc.optionMenu(label="Output node")

    for item in firstElementAttributes:
        mc.menuItem(label=item)

    InputNodesOptionMenu = mc.optionMenu(label="Input Nodes")

    for item in secondElementAttribtues:
        mc.menuItem(label=item)
        


    #create visuallizers of what nodes are selected
    mc.text(OutputNode, annotation="Output Node", height=20, backgroundColor = [0.01, 0.01, 0.01] )

    mc.text(InputNodes, annotation="Input Nodes", height=20, backgroundColor = [0.3, 0.3, 0.3] )

    #execution button to connect the inputs and outputs
    mc.button(label='Build Swtich', command=lambda _: ConnectOneToNNodes(mc.optionMenu(OutputNodeOptionMenu, query=True, value=True), mc.optionMenu(InputNodesOptionMenu, query=True, value=True), OutputNode, InputNodes, sel))


    #Display The window
    mc.showWindow(configWindow)