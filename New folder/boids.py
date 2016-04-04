##	http://www.kfish.org/boids/pseudocode.html
##	http://vpython.org/contents/contributed/boids.py

import maya.cmds as cmds
import random
import maths

class Boids:
	def __init__(self, Rules = [True, True, True, True, True, False, False, False, False], numboids = 10, boundsBoxSize = [100.0,100.0,100.0]):
		self.Wind = 10
		self.Rules = Rules
		self.BoidNumber = numboids
		#self.BoxBoundry = []
		self.BoxBoundry	= boundsBoxSize
		#Create Bounds box
		cmds.polyCube( n='Boundies', w = self.BoxBoundry.[0], h = self.BoxBoundry.[1], d = self.BoxBoundry.[2])
		self.AgentsList = []
		
		
		self.separationDistance = 100
		
		#Biases
		self.separationBias = 0.1
		self.alignemtBias = 0.1
		self.cohesionBias = 0.1
		
		for x in range(0,self.BoidNumber):
			CreateAgent(self.BoidNumber)

	def run(self):
		pass
	
	def CreateAgent(self, number):
		##Seting up Names
		agent_name = 'Agent_' + str(number)
		
		## Setting up random Positions
		initPos = []
		initPos.append(random.random(-self.BoxBoundry[0]/2.0,self.BoxBoundry[0]/2.0)
		initPos.append(random.random(-self.BoxBoundry[1]/2.0,self.BoxBoundry[1]/2.0)
		initPos.append(random.random(-self.BoxBoundry[2]/2.0,self.BoxBoundry[2]/2.0)
		
		## Setting up random Velocities
		initVol = []
		initVol.append(random.random(-1.0,1.0))
		initVol.append(random.random(-1.0,1.0))
		initVol.append(random.random(-1.0,1.0))
		
		##Creating agent and adding to the list.
		self.AgentsList.append(Agent(agent_name, initPos, initVol)

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
		cmds.delete(ch=True)
		
	def initPos(self):
		pass
		
	def moveAll(self):
		
		
		
		for b in self.AgentsList:
			CheckingNeighbours(b)
			if self.Rules[0] == True:		# Rule 1: Separation
				Separation(b)
			else if self.Rules[1] == True:	# Rule 2: Alignment
				Alignment(b)
			else if self.Rules[2] == True:	# Rule 3: Cohesion
				Cohesion(b)
			else if self.Rules[3] == True:	# Rule 4: LimitSpeed
				pass
			else if self.Rules[4] == True:	# Rule 5: OutofBounds
				pass
			else if self.Rules[5] == True:	# Rule 6: Wind
				pass
			else if self.Rules[6] == True:	# Rule 7: TendTowardsGoal
				pass
			else if self.Rules[7] == True:	# Rule 8: FleeTargetLocation
				pass
			else if self.Rules[8] == True:	# Rule 9: ObjectAvoidance
				pass
		
	def CheckingNeighbours(self, aBoid):
		NeiList = []
		for b in self.AgentsList:
			if aboid != b:
				if sqrt(pow(aboid.currentPosition[0] - b.currentPositionp[0],2) + pow(aboid.currentPosition[1] - b.currentPositionp[2],2) + pow(aboid.currentPosition[0] - b.currentPositionp[2],2)) <=25:
					NeiList.append(b)
		
		
		aboid.setNeighbours(NeiList)
		
	def Separation(self, aBoid): # Rule 1: Separation
	
		Separation = [0.0, 0.0, 0.0]
		for b in aBoid.neighboursList:
			if aboid != b:
				if sqrt(pow(aboid.currentPosition[0] - b.currentPositionp[0],2) + pow(aboid.currentPosition[1] - b.currentPositionp[2],2) + pow(aboid.currentPosition[0] - b.currentPositionp[2],2)) <= self.separationDistance:
					Separation = [(aboid.currentPosition[0] - b.currentPositionp[0]), 
		
		
		return 

	def Alignment(self, aBoid): # Rule 2
		pass
	
	def Cohesion(self, aBoid): # Rule 3
		pass
	
	def LimitSpeed(self, aBoid): # Rule 4
		pass
	
	def OutofBounds(self, aBoid): # Rule 5
		#if aboid pos x < top_bound
		pass
	
	def Wind(self, aBoid): #Rule 6
		return self.Wind
	
	def TendTowardsGoal(self, aBoid): # Rule 7
		pass
	
	def FleeTargetLocation(self, aBoid, aTarget): # Rule 8
		pass
	
	def ObjectAvoidance(self, aBoid, aObject): # Rule 9
		pass
		# Sphere, Cylinder and Cube
	
		
		
class Agent(object):
	def __init__(self, Name = 'Agent' , position = [0.0,0.0,0.0], velocity = [1.0,0.0,0.0], viewRadius = 120, ):
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