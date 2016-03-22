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

# this function is used to initialise the simulation
def init():
    print "Custom simulation initialised"
    # reset last frame counter
    global last_frame_number
    last_frame_number = 1
    
    # INSERT SCRIPT HERE TO PERFORM ANY INITIALISATION OF THE SIMULATION
    
    
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

# ADD ANY OF YOUR OWN SCRIPT FUNCTIONS HERE
