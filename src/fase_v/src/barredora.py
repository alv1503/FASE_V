#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge
import numpy as np
from geometry_msgs.msg import Twist
from time import sleep

if __name__ == '__main__':
    try:
        # Inicializar nodo y publisher

        rospy.init_node('robot_mover', anonymous=True)
        mov_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        speed = Twist()
        i = 0

        # Adelante
        i = 0
        while i < 1000:
            speed.linear.x = 0.5
            speed.angular.z = 0.0
            mov_pub.publish(speed)
            rospy.sleep(50)

        # Atrás
        i = 0
        while i < 1000:
            speed.linear.x = -0.5
            speed.angular.z = 0.0
            mov_pub.publish(speed)
            rospy.sleep(50)

        # Girar
        i = 0
        while i < 10:
            speed.linear.x = 0.0
            speed.angular.z = 0.1
            mov_pub.publish(speed)
            rospy.sleep(50)

    
    except rospy.ROSInterruptException:
        pass