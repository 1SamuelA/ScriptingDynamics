import maya.cmds as cmds
import maya.mel as mel
import math

# GLOBAL VARIABLES
#
# These are variables the are used across more than one function
# e.g. last_frame_number is used in the init function and the run function
# when we want to use these variables in a function we need to inidicate it is in fact
# a global variable using the global keyword

# last_frame_number stores the frame number of the last successful run of the simulation
# this is needed to prevent any odd behaviour if the timeline is played backwards
# or if we jump to a particular frame.
# we need to simulate every frame so we don't miss any events
last_frame_number = 1
agent0_name = "pCone1"

# this function is used to initialise the simulation
def init():
	print "Custom simulation initialised"
	# reset last frame counter
	global last_frame_number
	last_frame_number = 1
	global agent0_name
	agent0_name = "pCone1"
	
	if cmds.objExists(agent0_name) is False:
	    cmds.polyCone(sx=4, n = agent0_name)
	    print "Cone Made"
	    cmds.setAttr( agent0_name+".rotateY",45.0)
	    cmds.setAttr( agent0_name+".rotateZ",90.0)
	    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
	    cmds.setAttr( agent0_name+".scaleY" ,0.75)
	    cmds.setAttr( agent0_name+".rotateY" ,90.0)
	    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0)
	    cmds.delete(ch=True)
	    
	agent_setup(agent0_name)
	
def agent_setup(agent_name):
	cmds.setAttr( agent_name+".translateX",0.0)
	cmds.setAttr( agent_name+".translateZ",0.0)

	cmds.setAttr( agent_name+".rotateY",0.0)
    
	if cmds.objExists(agent_name+".speed") is False:
		print "Speed Added"
		cmds.select(agent_name)
		cmds.addAttr( longName = "Speed",shortName="speed", attributeType="float", keyable = True)
	
	cmds.setAttr( agent_name+".speed",10.0)
    
	if cmds.objExists(agent_name+".rotSpeed") is False:
		print "Rotation Speed Added"
		cmds.select(agent_name)
		cmds.addAttr( longName = "rotSpeed",shortName="rotspe", attributeType="float", keyable = True) 
	cmds.setAttr( agent_name+".rotSpeed",1.0)
    
	if cmds.objExists(agent_name+".rotLerp") is False:
		print "Rotation Lerp Added"
		cmds.select(agent_name)
		cmds.addAttr( longName = "rotLerp",shortName="rotlerp", attributeType="bool", keyable = True) 
	cmds.setAttr( agent_name+".rotLerp", False)
    
# this function is called every frame the simulation is run
def run(frame_number):
    
	# get the frame rate by using an internal MEL script
	frame_rate = mel.eval("currentTimeUnitToFPS")
    
	# calculate the amount of time in seconds between each frame
	frame_time = 1.0 / frame_rate
    
	# special case if we are on the first frame then initialise the simulation
	if frame_number == 1:
		init()
		
	# check to see if we have an event to process this frame
	global last_frame_number
	if (frame_number - last_frame_number) == 1:
		# INSERT SCRIPT HERE TO RUN THE SIMULATION HERE
        
		print "Custom simulation run successfully at frame: "+str(frame_number)
		
		# we have successfully completed a run of the simulation
		# update the last frame number
		last_frame_number = frame_number
		
	if frame_number > 1:
		
		agent_move(agent0_name, frame_time)
    
# ADD ANY OF YOUR OWN SCRIPT FUNCTIONS HERE
def agent_move(agent, time):
	if cmds.getAttr(agent+".rotLerp") is True:
		heading = cmds.getAttr(agent+".rotateY") * cmds.getAttr(agent+".rotSpe")
		print "Lerping"
	else:
		heading = cmds.getAttr(agent+".rotateY")
		print "NLerping"
		
	distance = time * cmds.getAttr(agent+".speed")
	print heading
	print distance
	
	initXPos = cmds.getAttr(agent+".translateX")
	initZPos = cmds.getAttr(agent+".translateZ")
    
	print initZPos
    
	xTraveled = distance*math.sin(math.radians(heading))
	zTraveled = distance*math.cos(math.radians(heading))
    
    
    
	cmds.setAttr( agent+".translateX",initXPos+xTraveled)
	cmds.setAttr( agent+".translateZ",initZPos+zTraveled)
    
    