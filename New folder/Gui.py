# SkelitonRigTool.py

import maya.cmds as cmds
import os as os
import maya.OpenMaya as om
import functools

def createUI( pWindowTitle, pCreateAgent):
    
    windowID = 'myWindowID'
    
    if cmds.window( windowID, exists=True ):
        cmds.deleteUI( windowID )
    
    cmds.window( windowID, title=pWindowTitle, sizeable=True, resizeToFitChildren=True )
    form = cmds.formLayout()
    tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
    cmds.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )
    
    BehaviourTab = cmds.rowColumnLayout( numberOfColumns=3, columnWidth=[ (1,140), (2,100), (3,90) ], columnOffset=[ (1,'right',3) ] )
    
    
    AlignmentBool = cmds.checkBox(label='Alignment Rule')

    
    CohesionBool = cmds.checkBox(label='Cohesion Rule')

    
    SeparationBool = cmds.checkBox(label='Separation Rule')
    
    
    def cancelCallback( *pArgs ):
        if cmds.window( windowID, exists=True ):
            cmds.deleteUI( windowID )
    
    cmds.button( label='Cancel', command=cancelCallback )
    cmds.setParent( '..' )
    
    cmds.tabLayout( tabs, edit=True, tabLabel=((BehaviourTab, 'Boid Behaviour')) )
    
    cmds.showWindow()
    
def createAgent():
    if cmds.objExists('Agent0') is False:
        agent_name = 'Agent0'
    else:
        
        cmds.selectType('Agent*')
        
        myList = cmds.ls('Agent*')
        print len(myList)
        num = len(myList) - 1
        print num
        agent_name = 'Agent' + str(num)
        
    cmds.select( clear=True )
    cmds.polyCone(sx=4, n = agent_name)
    print "Cone Made"
    cmds.setAttr( agent_name+".rotateY",45.0)
    cmds.setAttr( agent_name+".rotateZ",90.0)
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    cmds.setAttr( agent_name+".scaleY" ,0.75)
    cmds.setAttr( agent_name+".rotateY" ,90.0)
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
    cmds.delete(ch=True)
    
createUI( 'My Title', 'CreateAgent' )
