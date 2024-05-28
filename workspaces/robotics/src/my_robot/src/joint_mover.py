#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState
from math import sin, pi
import time

def pendulum_swing():
    rospy.init_node('pendulum_swing_publisher', anonymous=True)
    
    # Publisher to publish joint states
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    
    # Set the loop rate (in Hz)
    rate = rospy.Rate(10)  # 10 Hz
    
    # Initial state
    joint_state = JointState()
    joint_state.name = ['pendulum_joint']
    joint_state.position = [0.0]
    
    start_time = time.time()
    
    while not rospy.is_shutdown():
        # Calculate the elapsed time
        elapsed = time.time() - start_time
        
        # Update the joint angle: simple harmonic motion formula
        joint_state.position = [0.5 * sin(2 * pi * 0.5 * elapsed)]  # Amplitude of 0.5 rad, frequency of 0.5 Hz
        
        # Update the header timestamp
        joint_state.header.stamp = rospy.Time.now()
        
        # Publish the joint state
        pub.publish(joint_state)
        
        # Sleep for the remainder of the loop rate
        rate.sleep()

if __name__ == '__main__':
    try:
        pendulum_swing()
    except rospy.ROSInterruptException:
        pass
