import maya.cmds as cmds
import random
import math
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
        self.boxFrame = cmds.frameLayout(l='Simulation Box', cll=True)
        
        self.boxWidth = cmds.floatSliderGrp(l='Width', f = True, min=1, max=20, fieldMinValue=1.0, fieldMaxValue=1000.0, value=1, dc = self.ChangeBoxSize,cc =  self.ChangeBoxSize)
        self.boxHeight = cmds.floatSliderGrp(l='Height', f = True, min=1, max=20, fieldMinValue=1.0, fieldMaxValue=1000.0, value=1,dc =  self.ChangeBoxSize,cc =  self.ChangeBoxSize)
        self.boxDepth = cmds.floatSliderGrp(l='Depth', f = True, min=1, max=20, fieldMinValue=1.0, fieldMaxValue=1000.0, value=1, dc =  self.ChangeBoxSize,cc =  self.ChangeBoxSize)
        
        cmds.setParent(self.mainForm)
        #Animation
        self.animationFrame = cmds.frameLayout(l='Animation Settings', cll=True)
        
        self.aniFrames = cmds.intSliderGrp(l='Number of Frames', f = True, min=1, max=1000, fieldMinValue=1.0, fieldMaxValue=1000.0, value=200, dc =  self.ChangeFrameCount, cc = self.ChangeFrameCount)
        
        cmds.setParent(self.mainForm)
        
        self.RulesFrame = cmds.frameLayout(l='Simulation Settings', cll=True)
        
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

        self.simulationFrame = cmds.frameLayout(l='Simulation Settings', cll=True)
        
        self.numAgents = cmds.intSliderGrp(l='Number Agents', f = True, min=1, max=200, fieldMinValue=1.0, fieldMaxValue=200.0, value=10 )
        self.AlignmentRadius = cmds.floatSliderGrp(l='Alignment Radius', f = True, min=1, max=1000, fieldMinValue=1.0, fieldMaxValue=1000.0, value=200 )
        self.AlignmentBias = cmds.floatSliderGrp(l='Alignment Bias', f = True, min=0, max=2, fieldMinValue=0.0, fieldMaxValue=2.0, value=0.02 , pre = 4)
        self.CohesionRadius = cmds.floatSliderGrp(l='Cohesion Radius', f = True, min=1, max=1000, fieldMinValue=1.000, fieldMaxValue=1000.000, value=200.000 )
        self.CohesionBias = cmds.floatSliderGrp(l='Cohesion Bias', f = True, min=0, max=2, fieldMinValue=0.000, fieldMaxValue=2.000, value=0.006, pre = 4 )
        self.SeparationRadius = cmds.floatSliderGrp(l='Separation Radius', f = True, min=1, max=1000, fieldMinValue=1.0, fieldMaxValue=1000.0, value=200 )
        self.SeparationBias = cmds.floatSliderGrp(l='Separation Agents', f = True, min=0, max=2, fieldMinValue=0.0, fieldMaxValue=2.0, value=0.006 , pre = 4)
        
        cmds.setParent(self.mainForm)
        
        
        
        cmds.button(label="Simulate", command=self.StartSimulation)
        
        # show the window
        cmds.showWindow(self.window)
        # force window size
        cmds.window(self.window, e=True, wh=self.size)
        
    def ChangeBoxSize(self,*args):
        pass
        if cmds.objExists('Boundies') is True :
            cmds.select('Boundies')
            cmds.delete()
        
        cmds.polyCube( n='Boundies', w = cmds.floatSliderGrp(self.boxWidth, q=True,v=True), h = cmds.floatSliderGrp(self.boxHeight, q=True,v=True), d = cmds.floatSliderGrp(self.boxDepth, q=True,v=True))
        
    def ChangeFrameCount(self,*args):
        endTime = cmds.intSliderGrp(self.aniFrames, q=True,v=True)
        
        cmds.playbackOptions(aet = endTime, max = endTime)
    
    def StartSimulation(self, *args):
        
        ## Packing the Simulation rules
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
        ## Packing the number of Agents
        NumAgents = cmds.intSliderGrp(self.numAgents, q=True,v=True)
        
        ## Packing the BoxSize
        BoundingBoxSize = []
        BoundingBoxSize.append(cmds.floatSliderGrp(self.boxWidth, q=True,v=True))
        BoundingBoxSize.append(cmds.floatSliderGrp(self.boxHeight, q=True,v=True))
        BoundingBoxSize.append(cmds.floatSliderGrp(self.boxDepth, q=True,v=True))
        
        self.Simulation = Boids(Rules, NumAgents, BoundingBoxSize)
        
        ## Rules Radius and Bias



class Agent(object):
	def __init__(self, Name = 'Agent' , position = [0.0,0.0,0.0], velocity = [1.0,0.0,0.0], viewRadius = 120):
		self.Name = Name
		self.currentVelocity = velocity
		self.currentPosition = position
		self.heading = [0.0, 0.0]
		self.newPosition = self.currentPosition
		self.viewRadius = viewRadius
		
		self.neighboursList = []
		
	def SetPosition(self, coords = [0.0, 0.0, 0.0]):
	    pass
	def setNeighbours(self, mNeighbours = []):
		self.neighboursList = mNeighbours
		

class Boids:
	def __init__(self, Rules = [True, True, True, True, True, False, False, False, False], numboids = 10, boundsBoxSize = [100.0,100.0,100.0], numFrames = 200):
		self.Wind = 10
		self.Rules = Rules
		self.BoidNumber = numboids
		#self.BoxBoundry = []
		self.BoxBoundry	= boundsBoxSize
		#Create Bounds box
		
		self.MaxFrames = numFrames
		
		cmds.polyCube( n='Boundies', w = self.BoxBoundry[0], h = self.BoxBoundry[1], d = self.BoxBoundry[2])
		self.AgentsList = []
		
		
		self.separationDistance = 100
		
		#Biases
		self.separationBias = 0.1
		self.alignemtBias = 0.1
		self.cohesionBias = 0.1
		
		for x in range(0,self.BoidNumber):
			self.CreateAgent(x)
			
		self.run()
		
	def run(self):
		self.moveAll()
	
	def CreateAgent(self, number):
		##Seting up Names
		agent_name = 'Agent_' + str(number)
		
		## Setting up random Positions
		initPos = []
		initPos.append(random.uniform(-self.BoxBoundry[0]/2.0,self.BoxBoundry[0]/2.0))
		initPos.append(random.uniform(-self.BoxBoundry[1]/2.0,self.BoxBoundry[1]/2.0))
		initPos.append(random.uniform(-self.BoxBoundry[2]/2.0,self.BoxBoundry[2]/2.0))
		
		## Setting up random Velocities
		initVol = []
		initVol.append(random.uniform(-1.0,1.0))
		initVol.append(random.uniform(-1.0,1.0))
		initVol.append(random.uniform(-1.0,1.0))
		
		##Creating agent and adding to the list.
		self.AgentsList.append(Agent(agent_name, initPos, initVol,120))

		## Create Mesh
		cmds.select( clear=True )
		cmds.polyCone(sx=4, n = agent_name)
		print "Cone Made"
		cmds.setAttr( agent_name+".rotateY",45.0)
		cmds.setAttr( agent_name+".rotateZ",90.0)
		cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
		cmds.setAttr( agent_name+".scaleY" ,0.75)
		cmds.setAttr( agent_name+".rotateY" ,90.0)
		cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
		cmds.setAttr( agent_name+".scaleX" ,0.5)
		cmds.setAttr( agent_name+".scaleY" ,0.5)
		cmds.setAttr( agent_name+".scaleZ" ,0.5)
		cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
		cmds.delete(ch=True)
		cmds.setAttr( agent_name+".scaleX" ,0.5)
		cmds.setAttr( agent_name+".scaleY" ,0.5)
		cmds.setAttr( agent_name+".scaleZ" ,0.5)
		cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
		cmds.delete(ch=True)
		
		cmds.setAttr( agent_name+".translateX" ,self.AgentsList[-1].currentPosition[0])
		cmds.setAttr( agent_name+".translateY" ,self.AgentsList[-1].currentPosition[1])
		cmds.setAttr( agent_name+".translateZ" ,self.AgentsList[-1].currentPosition[2])
		
	def initPos(self):
		pass
		
	def moveAll(self):
	    
		for b in self.AgentsList:
		    print b.Name
		    vF = [0.0,0.0,0.0]
		    v1 = []
		    v2 = []
		    v3 = []
		    self.CheckingNeighbours(b)
		    
		    if self.Rules[0] == True:
		        self.Separation(b)
	def CheckingNeighbours(self, aBoid = Agent):
		NeiList = []
		for b in self.AgentsList:
			if aBoid != b:
				if math.sqrt(pow(aBoid.currentPosition[0] - b.currentPosition[0],2) + pow(aBoid.currentPosition[1] - b.currentPosition[2],2) + pow(aBoid.currentPosition[0] - b.currentPosition[2],2)) <=2:
					NeiList.append(b.Name)
		
		print NeiList
		aBoid.setNeighbours(NeiList)
		
	def Separation(self, aBoid = Agent): # Rule 1: Separation
	    
	    Separation = [0.0, 0.0, 0.0]
	    for b in aBoid.neighboursList:
	        print str(2) 
	    
        

	def Alignment(self,  aBoid = Agent( 'Agent' , [0.0,0.0,0.0],[1.0,0.0,0.0], 120)): # Rule 2
		pass
	
	def Cohesion(self,  aBoid = Agent( 'Agent' , [0.0,0.0,0.0],[1.0,0.0,0.0], 120)): # Rule 3
		pass
	
	
		# Sphere, Cylinder and Cube



GUI = GUI_Flocking
GUI.showUI()







