import maya.cmds as cmds
import maya.OpenMaya as om
import os.path

import functools

Speed = 0.0
RotLerpSpeed = 0.0
RotLerp = False

def CreateDataFile(PATH):
    print('Creating new text file') 
    
    try:
        file = open(PATH,'a')   # Trying to create a new file or open one
        file.write('# This is the Data for the script')
        file.write('')	
        file.write('# default Speed')
        file.write('10.0')
        file.write('# default Rotate Lerp Speed')
        file.write('10.0')
        file.write('# default Rotate Lerp Bool')
        file.write('0')
        file.close()

    except:
        print('Something went wrong! Can\'t tell what?')
        sys.exit(0) # quit Python



def createUI( pWindowTitle):
    
    windowID = 'myWindowID'
    PATH='./Data.txt'

    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        print "File exists and is readable"
    else:
       print "Either file is missing or is not readable" 
       CreateDataFile(PATH)
    
    if cmds.window( windowID, exists=True ):
        cmds.deleteUI( windowID )
    
    cmds.window( windowID, title=pWindowTitle, sizeable=True, resizeToFitChildren=True )
    form = cmds.formLayout()
    tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)
    cmds.formLayout( form, edit=True, attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)) )
    
    Start = cmds.rowColumnLayout( numberOfColumns=3, columnWidth=[ (1,140), (2,100), (3,90) ], columnOffset=[ (1,'right',3) ] )
    
    
    cmds.text( label='Number of Spine pieces:' )
    numSpineField = cmds.intField(value = 1)
    wristTwistField = cmds.checkBox(label='Wrist Twist')
    cmds.text( label='Attribute:' )
    targetAttributeField = cmds.textField( text='' )
    aPositionField = cmds.checkBox(label='A-Position')
    
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
    complexHandField = cmds.checkBox(label='Complex Hand')
    
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
    cmds.separator( h=10, style='none' )
    
    
    cmds.button( label='Build Bones')
    cmds.button( label='Build IKs')
    
    def cancelCallback( *pArgs ):
        if cmds.window( windowID, exists=True ):
            cmds.deleteUI( windowID )
    
    cmds.button( label='Cancel', command=cancelCallback )
    cmds.setParent( '..' )
    
    cmds.tabLayout( tabs, edit=True, tabLabel=((Start, 'Start')) )
    
    cmds.showWindow()
    
    
createUI( 'My Title')