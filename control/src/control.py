#! /usr/bin/env python
from __future__ import print_function
import sys
import rospy
import tf2_ros
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import math
import numpy as np
rospy.set_param('gripper',0)
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node("final_node", anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group_name = "arm"
move_group = moveit_commander.MoveGroupCommander(group_name)
group1_name = "gripper"
gripper_group = moveit_commander.MoveGroupCommander(group1_name)
#display_trajectory_publisher = rospy.Publisher("/move_group/display_planned_path",moveit_msgs.msg.DisplayTrajectory,queue_size=20)
value=0
value1=0
value2=0
print('hello')
rate = rospy.Rate(10) 
while not rospy.is_shutdown():

	file=open('/home/srinir/catkin_ws/src/HardWired/control/src/gesture.txt','r')
	value=file.read()
	if value=='4' and value1=='4' and value2=='4':
		joint_goal = move_group.get_current_joint_values()
		joint_goal[0] = 0
		joint_goal[1] = 1.57
		joint_goal[2] = -70*3.14/180
		move_group.go(joint_goal, wait=True)
		move_group.stop()
	if value=='5' and value1=='5' and value2=='5':
		file=open('/home/srinir/catkin_ws/src/HardWired/control/src/dice.txt','r')
		dice=int(file.read())
		joint_goal = move_group.get_current_joint_values()
		joint_goal[0] = dice*30*3.14/180
		joint_goal[1] = 20*3.14/180
		joint_goal[2] = 0
		move_group.go(joint_goal, wait=True)
		move_group.stop()
	if value=='1' and value1=='1' and value2=='1':
		rospy.set_param('gripper',1)
	value1=value
	value2=value1
	print(value,value1,value2)
	rate.sleep()
