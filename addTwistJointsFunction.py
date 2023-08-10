import maya.cmds as cmds


twistjointCount = 5


sel = cmds.ls(selection=True)

firstJoint = sel[0]
secondJoint = sel[1]

twistJoints = []

for i in range(twistjointCount):
    cmds.select(clear=True)
    newTwistJoint = cmds.joint()
    twistJoints.append(newTwistJoint)
    

firstweights = []
secondweights = []

for i in range(len(twistJoints)):
    newPointConstraint = cmds.pointConstraint(firstJoint, secondJoint, twistJoints[i -1], w=1)
    
    initial_value = 100
    iteration_count = (twistjointCount - 1) / 2
    recursive_splits = recursive_split(initial_value, iteration_count, 2)
    
    weight1 = i/twistjointCount
    weight2 = abs(weight1 - 1)
    
    print(weight1, weight2)
    
    
    cmds.setAttr(newPointConstraint[0] + "." + firstJoint + "W0", weight2)
    cmds.setAttr(newPointConstraint[0] + "." + secondJoint + "W1", weight1)
    
  
def recursive_split(value, n, factor):
    if n == 0:
        return [value]
    else:
        divided_value = value / factor
        sub_results = recursive_split(divided_value, n - 1, factor)
        return [value] + sub_results


print(recursive_splits)  # Output: [100, 50.0, 25.0, 12.5]
    