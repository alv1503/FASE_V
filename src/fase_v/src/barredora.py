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
    except rospy.ROSInterruptException:
        pass