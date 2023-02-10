#!/usr/bin/env python

import rospy

from sensor_msgs.msg import JointState as JointStateMoveIt
from dynamixel_msgs.msg import JointState as JointStateDynamixel

class JointStateMessage():
    def __init__(self, name, position, velocity, effort):
        self.name = name
        self.position = position
        self.velocity = velocity
        self.effort = effort

class JointStatePublisher():
    def __init__(self):
        rospy.init_node('finalarm_joint_state_publisher')

        rate = 50 # 20Hz
        r = rospy.Rate(rate)

        self.joint1name = ''
        self.joint1current_pos = 0.0
        self.joint1velocity = 0.0
        self.joint1load = 0.0

        self.joint2name = ''
        self.joint2current_pos = 0.0
        self.joint2velocity = 0.0
        self.joint2load = 0.0

        self.joint3name = ''
        self.joint3current_pos = 0.0
        self.joint3velocity = 0.0
        self.joint3load = 0.0

        self.joint4name = ''
        self.joint4current_pos = 0.0
        self.joint4velocity = 0.0
        self.joint4load = 0.0

        self.joint5name = ''
        self.joint5current_pos = 0.0
        self.joint5velocity = 0.0
        self.joint5load = 0.0

        self.joint6name = ''
        self.joint6current_pos = 0.0
        self.joint6velocity = 0.0
        self.joint6load = 0.0

        self.joint7name = ''
        self.joint7current_pos = 0.0
        self.joint7velocity = 0.0
        self.joint7load = 0.0

        self.joint8name = ''
        self.joint8current_pos = 0.0
        self.joint8velocity = 0.0
        self.joint8load = 0.0

        self.joint9name = ''
        self.joint9current_pos = 0.0
        self.joint9velocity = 0.0
        self.joint9load = 0.0

        # Start controller state subscribers
        rospy.Subscriber('/finalarm_position_controller_1/state', JointStateDynamixel, self.controller_state_handler_1)
        rospy.Subscriber('/finalarm_position_controller_2/state', JointStateDynamixel, self.controller_state_handler_2)
        rospy.Subscriber('/finalarm_position_controller_3/state', JointStateDynamixel, self.controller_state_handler_3)
        rospy.Subscriber('/finalarm_position_controller_4/state', JointStateDynamixel, self.controller_state_handler_4)
        rospy.Subscriber('/finalarm_position_controller_5/state', JointStateDynamixel, self.controller_state_handler_5)
        rospy.Subscriber('/finalarm_position_controller_6/state', JointStateDynamixel, self.controller_state_handler_6)
        rospy.Subscriber('/finalarm_position_controller_7/state', JointStateDynamixel, self.controller_state_handler_7)
        rospy.Subscriber('/finalarm_position_controller_8/state', JointStateDynamixel, self.controller_state_handler_8)
        rospy.Subscriber('/finalarm_position_controller_9/state', JointStateDynamixel, self.controller_state_handler_9)

        # Start publisher
        self.joint_states_pub = rospy.Publisher('/joint_states', JointStateMoveIt)

        rospy.loginfo("Publishing joint_state at " + str(rate) + "Hz")

        while not rospy.is_shutdown():
            self.publish_joint_states()
            r.sleep()

    def controller_state_handler_1(self, msg):
        self.joint1name = msg.name
        self.joint1current_pos = msg.current_pos
        self.joint1velocity = msg.velocity
        self.joint1load = msg.load

    def controller_state_handler_2(self, msg):
        self.joint2name = msg.name
        self.joint2current_pos = msg.current_pos
        self.joint2velocity = msg.velocity
        self.joint2load = msg.load

    def controller_state_handler_3(self, msg):
        self.joint3name = msg.name
        self.joint3current_pos = msg.current_pos
        self.joint3velocity = msg.velocity
        self.joint3load = msg.load

    def controller_state_handler_4(self, msg):
        self.joint4name = msg.name
        self.joint4current_pos = msg.current_pos
        self.joint4velocity = msg.velocity
        self.joint4load = msg.load

    def controller_state_handler_5(self, msg):
        self.joint5name = msg.name
        self.joint5current_pos = msg.current_pos
        self.joint5velocity = msg.velocity
        self.joint5load = msg.load

    def controller_state_handler_6(self, msg):
        self.joint6name = msg.name
        self.joint6current_pos = msg.current_pos
        self.joint6velocity = msg.velocity
        self.joint6load = msg.load

    def controller_state_handler_7(self, msg):
        self.joint7name = msg.name
        self.joint7current_pos = msg.current_pos
        self.joint7velocity = msg.velocity
        self.joint7load = msg.load

    def controller_state_handler_8(self, msg):
        self.joint8name = msg.name
        self.joint8current_pos = msg.current_pos
        self.joint8velocity = msg.velocity
        self.joint8load = msg.load

    def controller_state_handler_9(self, msg):
        self.joint9name = msg.name
        self.joint9current_pos = msg.current_pos
        self.joint9velocity = msg.velocity
        self.joint9load = msg.load

    def publish_joint_states(self):
        # Construct message & publish joint states
        msg = JointStateMoveIt()
        msg.name = []
        msg.position = []
        msg.velocity = []
        msg.effort = []

        msg.name.append(self.joint1name)
        msg.position.append(self.joint1current_pos)
        msg.velocity.append(self.joint1velocity)
        msg.effort.append(self.joint1load)

        msg.name.append(self.joint2name)
        msg.position.append(self.joint2current_pos)
        msg.velocity.append(self.joint2velocity)
        msg.effort.append(self.joint2load)

        msg.name.append(self.joint3name)
        msg.position.append(self.joint3current_pos)
        msg.velocity.append(self.joint3velocity)
        msg.effort.append(self.joint3load)

        msg.name.append(self.joint4name)
        msg.position.append(self.joint4current_pos)
        msg.velocity.append(self.joint4velocity)
        msg.effort.append(self.joint4load)

        msg.name.append(self.joint5name)
        msg.position.append(self.joint5current_pos)
        msg.velocity.append(self.joint5velocity)
        msg.effort.append(self.joint5load)

        msg.name.append(self.joint6name)
        msg.position.append(self.joint6current_pos)
        msg.velocity.append(self.joint6velocity)
        msg.effort.append(self.joint6load)

        msg.name.append(self.joint7name)
        msg.position.append(self.joint7current_pos)
        msg.velocity.append(self.joint7velocity)
        msg.effort.append(self.joint7load)

        msg.name.append(self.joint8name)
        msg.position.append(self.joint8current_pos)
        msg.velocity.append(self.joint8velocity)
        msg.effort.append(self.joint8load)

        msg.name.append(self.joint9name)
        msg.position.append(self.joint9current_pos)
        msg.velocity.append(self.joint9velocity)
        msg.effort.append(self.joint9load)

        msg.header.stamp = rospy.Time.now()
        msg.header.frame_id = 'base_link'
        self.joint_states_pub.publish(msg)

if __name__ == '__main__':
    try:
        s = JointStatePublisher()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
