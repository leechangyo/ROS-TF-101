#!/usr/bin/env python
import rospy
import tf

if __name__ == '__main__':
    rospy.init_node('fixed_frame_broadcaster')
    br = tf.TransformBroadcaster()
    rate = rospy.Rate(5)
    while not rospy.is_shutdown():
        br.sendTransform((1.0, 0.0, 0.0),
                        (0, 0, 0, 1),
                        rospy.Time.now(),
                        "fixed_carrot",
                        "turtle1")
        rate.sleep()