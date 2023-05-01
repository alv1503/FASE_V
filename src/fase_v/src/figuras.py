#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from math import pi, sqrt

'''
Ajustado para que dibuje las figuras correctas
'''

if __name__ == '__main__':
    try:
        # Inicializar nodo y publisher

        rospy.init_node('robot_mover', anonymous=True)
        mov_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rate = rospy.Rate(10)

        # Pedir al usuario que introduzca el movimiento que quiere realizar

        opcion = ''
        while opcion != 'cuadrado' or opcion != 'circulo':
            opcion = input("Introduce 'cuadrado', 'rectangulo' o 'triangulo': ")
            if opcion == 'cuadrado':
                # move forward 20 cm and turn right 90 degrees, four times to form a square
                for i in range(4):
                # move forward 20 cm
                    vel_msg = Twist()
                    vel_msg.linear.x = 0.1 # m/s
                    vel_msg.angular.z = 0 # rad/s
                    distance = 0.2 # m
                    time_to_move = distance / vel_msg.linear.x

                    t0 = rospy.Time.now().to_sec()
                    current_distance = 0

                    while current_distance < distance:
                        mov_pub.publish(vel_msg)
                        t1 = rospy.Time.now().to_sec()
                        current_distance = vel_msg.linear.x * (t1 - t0)
                        rate.sleep()

                    # turn 90 degrees to the right
                    vel_msg.linear.x = 0 # m/s
                    vel_msg.angular.z = (pi/2)/5 # rad/s
                    time_to_turn = pi/2 / vel_msg.angular.z

                    t0 = rospy.Time.now().to_sec()
                    current_time = 0

                    while current_time < time_to_turn:
                        mov_pub.publish(vel_msg)
                        t1 = rospy.Time.now().to_sec()
                        current_time = t1 - t0
                        rate.sleep()

                # stop the robot
                vel_msg.linear.x = 0 # m/s
                vel_msg.angular.z = 0 # rad/s
                mov_pub.publish(vel_msg)
            elif opcion == 'rectangulo':
                # move forward 10 cm and turn right 90 degrees, move forward 30 cm and turn right 90 degrees, 
                # repeat 2 times to form a rectangle
                for i in range(2):
                    # move forward 10 cm
                    vel_msg = Twist()
                    vel_msg.linear.x = 0.1 # m/s
                    vel_msg.angular.z = 0 # rad/s
                    distance = 0.1 # m
                    time_to_move = distance / vel_msg.linear.x

                    t0 = rospy.Time.now().to_sec()
                    current_distance = 0

                    while current_distance < distance:
                        mov_pub.publish(vel_msg)
                        t1 = rospy.Time.now().to_sec()
                        current_distance = vel_msg.linear.x * (t1 - t0)

                    # stop the robot
                    vel_msg.linear.x = 0 # m/s
                    vel_msg.angular.z = 0 # rad/s
                    mov_pub.publish(vel_msg)

                    # turn 90 degrees to the right
                    vel_msg.linear.x = 0 # m/s
                    vel_msg.angular.z = (pi/2)/5 # rad/s
                    time_to_turn = pi/2 / vel_msg.angular.z

                    t0 = rospy.Time.now().to_sec()
                    current_time = 0

                    while current_time < time_to_turn:
                        mov_pub.publish(vel_msg)
                        t1 = rospy.Time.now().to_sec()
                        current_time = t1 - t0

                    # stop the robot
                    vel_msg.linear.x = 0 # m/s
                    vel_msg.angular.z = 0 # rad/s
                    mov_pub.publish(vel_msg)

                    # move forward 30 cm
                    vel_msg.linear.x = 0.1 # m/s
                    vel_msg.angular.z = 0 # rad/s
                    distance = 0.3 # m
                    time_to_move = distance / vel_msg.linear.x

                    t0 = rospy.Time.now().to_sec()
                    current_distance = 0

                    while current_distance < distance:
                        mov_pub.publish(vel_msg)
                        t1 = rospy.Time.now().to_sec()
                        current_distance = vel_msg.linear.x * (t1 - t0)

                    # stop the robot
                    vel_msg.linear.x = 0 # m/s
                    vel_msg.angular.z = 0 # rad/s
                    mov_pub.publish(vel_msg)

                    # turn 90 degrees to the right
                    vel_msg.linear.x = 0 # m/s
                    vel_msg.angular.z = (pi/2)/5 # rad/s
                    time_to_turn = pi/2 / vel_msg.angular.z

                    t0 = rospy.Time.now().to_sec()
                    current_time = 0

                    while current_time < time_to_turn:
                        mov_pub.publish(vel_msg)
                        t1 = rospy.Time.now().to_sec()
                        current_time = t1 - t0

                    # stop the robot
                    vel_msg.linear.x = 0 # m/s
                    vel_msg.angular.z = 0 # rad/s
                    mov_pub.publish(vel_msg)

                # stop the robot
                vel_msg.linear.x = 0 # m/s
                vel_msg.angular.z = 0 # rad/s
                mov_pub.publish(vel_msg)
            elif opcion == 'triangulo':
                # move forward 25 cm and turn left 120 degrees, repeat 3 times to form an equilateral triangle
                for i in range(3):
                    # move forward 25 cm
                    vel_msg = Twist()
                    vel_msg.linear.x = 0.1 # m/s
                    vel_msg.angular.z = 0 # rad/s
                    distance = 0.25 # m
                    time_to_move = distance / vel_msg.linear.x

                    t0 = rospy.Time.now().to_sec()
                    current_distance = 0

                    while current_distance < distance:
                        mov_pub.publish(vel_msg)
                        t1 = rospy.Time.now().to_sec()
                        current_distance = vel_msg.linear.x * (t1 - t0)

                    # stop the robot
                    vel_msg.linear.x = 0 # m/s
                    vel_msg.angular.z = 0 # rad/s
                    mov_pub.publish(vel_msg)

                    # turn 120 degrees to the left
                    vel_msg.linear.x = 0 # m/s
                    vel_msg.angular.z = (2*pi/3)/5 # rad/s
                    time_to_turn = 2*pi/3 / vel_msg.angular.z

                    t0 = rospy.Time.now().to_sec()
                    current_time = 0

                    while current_time < time_to_turn:
                        mov_pub.publish(vel_msg)
                        t1 = rospy.Time.now().to_sec()
                        current_time = t1 - t0

                    # stop the robot
                    vel_msg.linear.x = 0 # m/s
                    vel_msg.angular.z = 0 # rad/s
                    mov_pub.publish(vel_msg)

                # stop the robot
                vel_msg.linear.x = 0 # m/s
                vel_msg.angular.z = 0 # rad/s
                mov_pub.publish(vel_msg)
            else:
                print("Error, debes introducir 'cuadrado', 'rectangulo' o 'triangulo'.")
                break
    except rospy.ROSInterruptException:
        pass
