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
          "grey": np.array((72, 76, 86)),
          "red": np.array((3, 3, 84))}

center_color = "black"
left_color = "black"
right_color = "black"

# LIDAR DATA
front = 3

def lidar_callback(data):
    # GLOBAL VARIABLES
    global front
    
    # LIDAR INFORMATION
    front = data.ranges[0]
    
def camera_callback(data):
    # GLOBAL VARIABLES
    global center_color
    global left_color
    global right_color
    
    # ROS IMAGE TO OPENCV
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    
    # GET IMAGE DIMENSIONS
    height, width, _ = cv_image.shape
    
    # GET THE CENTER, CENTER_LEFT AND CENTER_RIGHT PIXEL
    center_pixel = cv_image[int(height/2), int(width/2)]
    center_left_pixel = cv_image[int(height/2), 0]
    center_right_pixel = cv_image[int(height/2), int(width) - 1]
    
    # GET THE CURRENT COLOR
    for color, code in colors.items():
        if (colors[color] == center_pixel).all():
            center_color = color
        
        if (colors[color] == center_left_pixel).all():
            left_color = color
            
        if (colors[color] == center_right_pixel).all():
            right_color = color
            

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
    while True:
        # BASIC MOVE
        vel_msg.linear.x = 0.22
        vel_msg.angular.z = 0.0
        
        if center_color == "yellow": # YELLOW
            if front < 0.7: # TURN RIGHT IF CLOSE
                angular_iterations = 0
                while angular_iterations < 1800:
                    vel_msg.linear.x = 0.22
                    vel_msg.angular.z = -0.7
                    vel_publisher.publish(vel_msg)
                    angular_iterations += 1
                    r.sleep()
                    
        if center_color == "blue": # BLUE
            if left_color == "yellow": # LEFT WALL IS YELLOW (SECOND TURN)
                if front < 1.200:
                    angular_iterations = 0
                    while angular_iterations < 1800:
                        vel_msg.linear.x = 0.22
                        vel_msg.angular.z = -0.7
                        vel_publisher.publish(vel_msg)
                        angular_iterations += 1
                        r.sleep()
                        
            else: # ONLY FOCUS ON THE FRONT (6th TURN)
                if front < 0.7:
                    angular_iterations = 0
                    while angular_iterations < 1800:
                        vel_msg.linear.x = 0.22
                        vel_msg.angular.z = 0.7
                        vel_publisher.publish(vel_msg)
                        angular_iterations += 1
                        r.sleep()

        if center_color == "white": # WHITE
            if left_color == "grey": # LEFT WALL IS GREY (3rd TURN)
                angular_iterations = 0
                while angular_iterations < 1800:
                    vel_msg.linear.x = 0.22
                    vel_msg.angular.z = -0.7
                    vel_publisher.publish(vel_msg)
                    angular_iterations += 1
                    r.sleep()
                    
            elif left_color == "white" and right_color == "white": # ALL YOU SEE IS WHITE (5th TURN)
                if front < 0.7: 
                    angular_iterations = 0
                    while angular_iterations < 1800:
                        vel_msg.linear.x = 0.22
                        vel_msg.angular.z = 0.7
                        vel_publisher.publish(vel_msg)
                        angular_iterations += 1
                        r.sleep()
        
        if center_color == "red": # RED
            if right_color == "yellow": # RIGHT WALL IS YELLOW (4th TURN)
                if front < 1:
                    angular_iterations = 0
                    while angular_iterations < 1800:
                        vel_msg.linear.x = 0.22
                        vel_msg.angular.z = 0.7
                        vel_publisher.publish(vel_msg)
                        angular_iterations += 1
                        r.sleep()
        
        vel_publisher.publish(vel_msg)
        r.sleep()
        
    rospy.spin()

    vel_msg.linear.x = 0.0
    vel_msg.angular.z = 0.0
    vel_publisher.publish(vel_msg)
    
