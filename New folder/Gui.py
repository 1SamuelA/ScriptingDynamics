import maya.cmds as cmds
import os as os
import maya.OpenMaya as om
import functools

class GUI_Flocking(object):
    @classmethod
    def showUI(cls):
        win = cls()
        win.create()
        return win
    def __init__(self):
        	
        # Window handle
        self.window = 'gui_flocking'
        self.title = 'Flocking Simulator'
        self.size = (420, 500)
        
    def create(self):
        # delete the window if its handle exists
        if(cmds.window(self.window, exists=True)):
            cmds.deleteUI(self.window, window=True)
        # initialize the window
        self.window = cmds.window(self.window, title=self.title, wh=self.size, s=False)
        # main form layout
        scrollLayout = cmds.scrollLayout(horizontalScrollBarThickness=16)
        
        self.mainForm = cmds.columnLayout(columnAttach=('left', 5), rowSpacing=0, columnWidth=400 )
        
        
        #Simulation Box Attributes layout
        self.boxFrame = cmds.frameLayout(l='Simulation Box')
        
        self.boxWidth = cmds.floatSliderGrp(l='Width', f = True, min=1, max=20, fieldMinValue=1.0, fieldMaxValue=100.0, value=1 )
        self.boxHeight = cmds.floatSliderGrp(l='Height', f = True, min=1, max=20, fieldMinValue=1.0, fieldMaxValue=100.0, value=1 )
        self.boxDepth = cmds.floatSliderGrp(l='Depth', f = True, min=1, max=20, fieldMinValue=1.0, fieldMaxValue=100.0, value=1 )
        
        cmds.setParent(self.mainForm)
        #Animation
        self.animationFrame = cmds.frameLayout(l='Animation Settings')
        
        self.aniFrames = cmds.floatSliderGrp(l='Number of Frames', f = True, min=1, max=1000, fieldMinValue=1.0, fieldMaxValue=1000.0, value=200 )
        
        cmds.setParent(self.mainForm)
        
        self.RulesFrame = cmds.frameLayout(l='Simulation Settings')
        
        self.RulesGrid = cmds.rowColumnLayout( numberOfColumns=4, columnWidth=[(1, 85), (2, 85),(3, 85),(4, 85) ],  columnSpacing=[(1, 10), (2, 10),(3, 10),(4, 10) ])
        
        self.buttonSeparation = cmds.checkBox( label='Separation' )
        self.buttonAlignment = cmds.checkBox( label='Alignment' )
        self.buttonCohesion = cmds.checkBox( label='Cohesion' )
        self.buttonLimitSpeed = cmds.checkBox( label='Limit Speed' )
        self.buttonOutofBounds = cmds.checkBox( label='Out of Bounds' )
        self.buttonWind = cmds.checkBox( label='Wind' )
        self.buttonGoals = cmds.checkBox( label='Goals' )
        self.buttonFleeTarget = cmds.checkBox( label='Flee Target' )
        
        cmds.setParent(self.mainForm)

        self.simulationFrame = cmds.frameLayout(l='Simulation Settings')
        
        self.numAgents = cmds.floatSliderGrp(l='Number Agents', f = True, min=1, max=1000, fieldMinValue=1.0, fieldMaxValue=1000.0, value=200 )
        self.AlignmentRadius = cmds.floatSliderGrp(l='Number Agents', f = True, min=1, max=1000, fieldMinValue=1.0, fieldMaxValue=1000.0, value=200 )
        self.AlignmentBias = cmds.floatSliderGrp(l='Number Agents', f = True, min=0, max=2, fieldMinValue=0.0, fieldMaxValue=2.0, value=0.02 )
        self.CohesionRadius = cmds.floatSliderGrp(l='Number Agents', f = True, min=1, max=1000, fieldMinValue=1.0, fieldMaxValue=1000.0, value=200 )
        self.CohesionBias = cmds.floatSliderGrp(l='Number Agents', f = True, min=0, max=2, fieldMinValue=0.0, fieldMaxValue=2.0, value=0.006 )
        self.SeparationRadius = cmds.floatSliderGrp(l='Separation Radius', f = True, min=1, max=1000, fieldMinValue=1.0, fieldMaxValue=1000.0, value=200 )
        self.SeparationBias = cmds.floatSliderGrp(l='Separation Agents', f = True, min=0, max=2, fieldMinValue=0.0, fieldMaxValue=2.0, value=0.006 )
        
        cmds.setParent(self.mainForm)
        
        cmds.button(label="Simulate", command=self.StartSimulation)
        
        # show the window
        cmds.showWindow(self.window)
        # force window size
        cmds.window(self.window, e=True, wh=self.size)
    
    def StartSimulation(self, *args):
        Rules = []
        Rules.append(cmds.checkBox(self.buttonSeparation, query=True, value=True))
        Rules.append(cmds.checkBox(self.buttonAlignment, query=True, value=True))
        Rules.append(cmds.checkBox(self.buttonCohesion, query=True, value=True))
        Rules.append(cmds.checkBox(self.buttonLimitSpeed, query=True, value=True))
        Rules.append(cmds.checkBox(self.buttonOutofBounds, query=True, value=True))
        Rules.append(cmds.checkBox(self.buttonWind, query=True, value=True))
        Rules.append(cmds.checkBox(self.buttonGoals, query=True, value=True))
        Rules.append(cmds.checkBox(self.buttonFleeTarget, query=True, value=True))
        
        print Rules
	
GUI = GUI_Flocking
GUI.showUI()















