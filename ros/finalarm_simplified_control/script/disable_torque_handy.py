#!/usr/bin/env python

import sys
import rospy
from dynamixel_controllers.srv import *
from dynamixel_msgs.msg import *

# Enable/disable motor torque
def set_torque_enable(joint, enable):
    torque_enable_srv = "finalarm_position_controller_{}/torque_enable".format(joint)
    rospy.wait_for_service(torque_enable_srv)
    try:
        torque_enable_req = rospy.ServiceProxy(torque_enable_srv, TorqueEnable)
        torque_enable_req(enable)
        print("(Joint: {}) Torque Enable set to {}".format(joint, enable))
    except rospy.ServiceException as e:
        print("(Joint: {}) Torque Enable service call failed: {}".format(joint, enable))

def usage():
    return "{}".format(sys.argv[0])

def main(num_joints):
    joint_list = [i+1 for i in range(num_joints)]
    rospy.init_node('disable_torque_handy')

    for joint in joint_list:
        # Disable 'torque enable' of current joint/motor
        set_torque_enable(joint, False)

if __name__ == "__main__":
    main(num_joints=9)
    rospy.sleep(0.5)
