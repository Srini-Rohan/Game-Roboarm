#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
from pyfirmata import Arduino,SERVO
from time import sleep
port = '/dev/ttyUSB0'
board = Arduino(port)
board.digital[2].mode = SERVO
board.digital[3].mode = SERVO
board.digital[4].mode = SERVO
board.digital[5].mode = SERVO
def rotateservo(pin,angle) :
    board.digital[pin].write(angle)
    sleep(0.015)

def callback(data):
    rotateservo(2,int(data.position[0]*180/3.14))
    rotateservo(3,int(data.position[1]*180/3.14))
    rotateservo(4,int(-data.position[2]*180/3.14))
    if rospy.get_param('gripper')==1:
	rotateservo(5,114)


def listener():
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber('/joint_states',JointState,callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
