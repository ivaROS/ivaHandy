#!/usr/bin/env python
import rospy
from .finalarm_joint_state_publisher import JointStatePublisher

if __name__ == '__main__':
    try:
        s = JointStatePublisher(num_joints=7)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
