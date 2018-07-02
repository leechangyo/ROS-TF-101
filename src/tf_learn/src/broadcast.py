#!/usr/bin/env python
import rospy
import time
import tf
from turtle_tf_3d.get_model_gazebo_pose import GazeboModel

def send_pose(pose_msg, robot_name):
    br = tf.TransformBroadcaster()
    
    br.sendTransform((pose_msg.position.x, pose_msg.position.y, pose_msg.position.z),
                    (pose_msg.orientation.x, pose_msg.orientation.y, pose_msg.orientation.z, pose_msg.orientation.w),
                    rospy.Time.now(),
                    robot_name,
                    "/world")
    
if __name__ == "__main__":
    rospy.init_node('turtle_tf_publisher', anonymous=True)
    robots = ["turtle1", "turtle2", "coke_can"]
    gazebo_model = GazeboModel(robots)
    
    for robot in robots:
        pose = gazebo_model.get_model_pose(robot)
        
    time.sleep(1)
    rospy.loginfo("Starting to push TF Data...")
    
    rate = rospy.Rate(5)
    while not rospy.is_shutdown():
        for robot in robots:
            pose = gazebo_model.get_model_pose(robot)
            if not pose:
                print("Pose not ready for", robot)
            else:
                send_pose(pose, robot)
        rate.sleep()
        