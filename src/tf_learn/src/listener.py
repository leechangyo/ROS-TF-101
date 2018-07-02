#!/usr/bin/env python
import rospy
import sys
import math
import tf
from geometry_msgs.msg import Twist

if __name__ == "__main__":
    rospy.init_node('turtle_follower')
    lstn = tf.TransformListener()
    follower = "turtle1"
    followee = "moving_carrot"
    
    vel_pub = rospy.Publisher(follower + "/cmd_vel", Twist)
    
    rate = rospy.Rate(10)
    ctrl_c = False
    
    follower_frame = "/" + follower
    followee_frame = "/" + followee
    
    def shutdownhook():
        global ctlr_c
        print("Shut 'er down!")
        vel = Twist()
        vel.linear.x = 0
        vel.angular.z = 0
        vel_pub.publish(vel)
        ctrl_c = True
        
    rospy.on_shutdown(shutdownhook)
    
    while not ctrl_c:
        try:
            (trans, rot) = lstn.lookupTransform(follower_frame, followee_frame, rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
        
        rospy.loginfo("Following!")
        angular = 4 * math.atan2(trans[1], trans[0])
        linear = .5 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)
        vel = Twist()
        vel.linear.x = linear
        vel.angular.z = angular
        vel_pub.publish(vel)
        
        rate.sleep()