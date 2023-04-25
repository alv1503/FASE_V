#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

'''
Falta indicar las distancias a recorrer, las velocidades correctas, tiempos de movimiento...
No he probado el código
'''

# Funciones publicadoras de mensajes

def movimiento_cuadrado():
    movimiento_msg = Twist()
    for i in range(4):
        # Mover recto
        movimiento_msg.linear.x = 0.5
        movimiento_msg.angular.z = 0.0
        mov_pub.publish(movimiento_msg)

        rospy.sleep(??)                         # Falta saber la distancia a recorrer, y dividirlo entre la velocidad lineal

        # Girar 90 grados
        movimiento_msg.linear.x = 0.0
        movimiento_msg.angular.z = ??           # Falta saber la velocidad angular y el tiempo que tarda en girar 90 grados
        mov_pub.publish(movimiento_msg)
        rospy.sleep(??)


def movimiento_circulo():
    movimiento_msg = Twist()
    movimiento_msg.linear.x = 0.5
    movimiento_msg.angular.z = ??               # Variable según el radio elegido
    mov_pub.publish(movimiento_msg)
    rospy.sleep(??)                             # Falta saber cuanto se tarda en dar una vuelta completa, variable según el radio elegido



# Ejecucion principal

if __name__ == '__main__':
    try:
        # Inicializar nodo y publisher

        rospy.init_node('robot_mover', anonymous=True)
        mov_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

        # Pedir al usuario que introduzca el movimiento que quiere realizar

        opcion = ''
        while opcion != 'cuadrado' or opcion != 'circulo':
            opcion = input("Introduce 'cuadrado' o 'circulo': ")
            if opcion == 'cuadrado':
                movimiento_cuadrado()
            elif opcion == 'circulo':
                movimiento_circulo()
            else:
                print("Error, debes introducir 'cuadrado' or 'circulo'.")
    except rospy.ROSInterruptException:
        pass
