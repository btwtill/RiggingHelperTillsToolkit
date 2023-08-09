import maya.cmds as mc


# filter a string list by another string list

def filter_strings(AttributeList, filterAttributes):
    filtered_strings = []
    
    for main_Attribute in AttributeList:
        for filter_string in filterAttributes:
            if filter_string in main_Attribute:
                filtered_strings.append(main_Attribute)
                break
    return filtered_strings


def duplicateSelection(selectionArray):
        dupList = []
        for i in selectionArray:
            newJoint = mc.duplicate(i, parentOnly=True)
            try:
                mc.parent(newJoint, world=True)
            except:
                print("already world Parent")
            dupList.append(newJoint)
            
        return dupList
            
def removeOneAndPrefixName(targetList, name):
            renamedList = []
            for i in range(len(targetList)):
                listElement = "".join(targetList[i])
                newName = listElement.replace("1", "")
                newName = name + newName
                renamedList.append(newName)
                mc.rename(targetList[i], newName)
            return renamedList



def reparenting(targetArray):
            for i in range(len(targetArray)):
                if i != (len(targetArray) - 1):
                    mc.parent(targetArray[i + 1], targetArray[i])