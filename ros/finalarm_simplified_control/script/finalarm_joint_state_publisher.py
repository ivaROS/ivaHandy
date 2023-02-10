#!/usr/bin/env python

import rospy

from sensor_msgs.msg import JointState as JointStateMoveIt
from dynamixel_msgs.msg import JointState as JointStateDynamixel
from functools import partial


class JointStatePublisher:
    def __init__(self, num_joints=9, rate=50):
        rospy.init_node("finalarm_joint_state_publisher")

        # a rate of 50 is 20Hz
        r = rospy.Rate(rate)

        self.num_joints = num_joints
        self.joint_states = [
            JointStateDynamixel(name="", current_pos=0.0, velocity=0.0, load=0.0)
            for _ in range(self.num_joints)
        ]

        # Start controller state subscribers
        for idx in range(self.num_joints):
            topic = "/finalarm_position_controller_{}/state".format(idx + 1)
            rospy.Subscriber(topic, JointStateDynamixel, partial(self.controller_state_handler, idx))

        # Start publisher
        self.joint_states_pub = rospy.Publisher("/joint_states", JointStateMoveIt, queue_size=100)

        rospy.loginfo("Publishing joint_state at {} Hz".format(rate))

        while not rospy.is_shutdown():
            self.publish_joint_states()
            r.sleep()

    def controller_state_handler(self, index, msg):
        self.joint_states[index] = msg

    def publish_joint_states(self):
        # Construct message & publish joint states
        msg = JointStateMoveIt()
        msg.name = []
        msg.position = []
        msg.velocity = []
        msg.effort = []

        for state in self.joint_states:
            msg.name.append(state.name)
            msg.position.append(state.current_pos)
            msg.velocity.append(state.velocity)
            msg.effort.append(state.load)

        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = "base_link"
        self.joint_states_pub.publish(msg)


if __name__ == "__main__":
    try:
        s = JointStatePublisher(num_joints=9)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
