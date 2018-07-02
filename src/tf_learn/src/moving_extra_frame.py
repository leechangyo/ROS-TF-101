#!/usr/bin/env python
import rospy
import tf
import math

if __name__ == '__main__':
    rospy.init_node('fixed_frame_broadcaster')
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(5)
    turning_rate = .1
    while not rospy.is_shutdown():
        t = .5*(rospy.Time.now().to_sec() * math.pi)
        rad_var = t % (2*math.pi)
        euler = (2+4 * math.sin(rad_var), 4 * math.cos(rad_var), 0)
        # euler = (0, 0, 0)1
        quat = (0, 0, 0, 1.0)
        br.sendTransform(euler, quat,
                        rospy.Time.now(),
                        "moving_carrot", 
                        "world")
        rate.sleep()