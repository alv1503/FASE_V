#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge
import numpy as np
from geometry_msgs.msg import Twist
from time import sleep

# COLORS INFO
colors = {"blue": np.array((69, 81, 44)),
          "white": np.array((116, 116, 116)),
          "yellow": np.array((31, 78, 102)),
          "grey": np.array((73, 76, 86)),
          "red": np.array((3, 3, 84))}

current_color = "black"

# MOVE CONTROL
move_forward = True

def lidar_callback(data):
    # GLOBAL VARIABLES
    global move_forward
    
    # LIDAR INFORMATION
    front = data.ranges[0]
    
    # STOP MOVING FORWARD
    if front < 1:
        move_forward = False
    
def camera_callback(data):
    # GLOBAL VARIABLES
    global current_color
    
    # ROS IMAGE TO OPENCV
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    
    # GET IMAGE DIMENSIONS
    height, width, _ = cv_image.shape
    # AND THE CENTER PIXEL
    center_pixel = cv_image[int(height/2), int(width/2)]
    
    # GET THE CURRENT COLOR
    for color, code in colors.items():
        if (colors[color] == center_pixel).all():
            current_color = color

if __name__ == "__main__":
    # INIT NODE AND SUBSCRIBERS/PUBLISHER
    rospy.init_node('color_maze', anonymous=True)
    lidar_subscriber = rospy.Subscriber("/scan", LaserScan, lidar_callback)
    camera_subscriber = rospy.Subscriber("/camera/rgb/image_raw", Image, camera_callback)
    vel_publisher = rospy.Publisher("/cmd_vel", Twist, queue_size = 10)
    r = rospy.Rate(1000)
    
    # TWIST MESSAGE
    vel_msg = Twist()
    
    # MOVES
    while move_forward: # MOVE FORWARD
        vel_msg.linear.x = 0.22
        vel_msg.angular.z = 0.0
        vel_publisher.publish(vel_msg)
        r.sleep()
    
    vel_msg.linear.x = 0.0
    vel_msg.angular.z = 0.0
    vel_publisher.publish(vel_msg)
    
    
    rospy.spin()
