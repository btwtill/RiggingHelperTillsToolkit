import maya.cmds as mc


def SuffixConfigurationWindow():
 #basic Window creation
    configWindow = mc.window(title="Suffix", iconName='Suffix', widthHeight=(200, 55), sizeable=True)
    
    #Window Layout
    mc.rowColumnLayout( adjustableColumn=True )
    
    #Label
    mc.text( label='Enter Suffix' )
    
    #Input Field Sotring the Stirng value
    name = mc.textField()
    
    #Building the switch execution button
    mc.button( label='OK', command=lambda _: suffixSelected(mc.textField(name, query=True, text=True)))
    

    #Display The window
    mc.showWindow(configWindow)

def suffixSelected(_suffix):

    #get user Selection
    sel = mc.ls(selection=True)

    #add suffix to the selected Items
    for i in sel:
        mc.rename(i, i + _suffix)
