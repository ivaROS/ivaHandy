#!/usr/bin/env python

import rospy
from dynamixel_controllers.srv import TorqueEnable
from argparse import ArgumentParser

# Enable/disable motor torque
def set_torque_enable(model_name, joint, enable):
    torque_enable_srv = "{}_position_controller_{}/torque_enable".format(model_name, joint)
    rospy.wait_for_service(torque_enable_srv)
    try:
        torque_enable_req = rospy.ServiceProxy(torque_enable_srv, TorqueEnable)
        torque_enable_req(enable)
        print("(Joint: {}) Torque Enable set to {}".format(joint, enable))
    except rospy.ServiceException as e:
        print("(Joint: {}) Torque Enable service call failed: {}".format(joint, enable))

def parse_args():
    parser = ArgumentParser(description='Disable torque for all joints of Handy')
    parser.add_argument('--num_joints', type=int, default=9, help='Number of joints of Handy')
    parser.add_argument(
        "--model_name", type=str, default="finalarm", help="Name of the robot model"
    )
    args, _ = parser.parse_known_args()
    return args

def main():
    args = parse_args()
    joint_list = [i+1 for i in range(args.num_joints)]
    rospy.init_node('disable_torque_handy')

    for joint in joint_list:
        # Disable 'torque enable' of current joint/motor
        set_torque_enable(args.model_name, joint, False)

if __name__ == "__main__":
    main()
    rospy.sleep(0.5)
