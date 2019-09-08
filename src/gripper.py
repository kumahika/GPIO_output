#!/usr/bin/env python

import pigpio
import time
import rospy
#from geomtry_msgs.msg import Twist
from std_msgs.msg import Int64

def callback(msg):
    # pwm0: 12, 18
    # pwm1: 13, 19
    gpio_pin = 18
    control_flag = msg.data
    duration = rospy.get_param('/duration_gripper')
    pwm_duty = 750000
    pi = pigpio.pi()
    pi.set_mode(gpio_pin, pigpio.OUTPUT)

    if control_flag == 1:
         # 500 [Hz] 80% (open)
        print("Open")
        pi.hardware_PWM(gpio_pin, 500, 800000)
        time.sleep(duration)
        pi.set_mode(gpio_pin, pigpio.INPUT)
        pi.stop()

    elif control_flag == 2:
        # 500 [Hz] 60% (close)
        print("Close")
        pi.hardware_PWM(gpio_pin, 500, 600000)
        time.sleep(duration)
        pi.set_mode(gpio_pin, pigpio.INPUT)
        pi.stop()

    elif control_flag == 3:
        print("open and close")
        pi.hardware_PWM(gpio_pin, 500, 800000)
        time.sleep(duration)
        print("mid")
        pi.hardware_PWM(gpio_pin, 500, 600000)
        time.sleep(duration)
        pi.set_mode(gpio_pin, pigpio.INPUT)
        pi.stop()

    else:
        print("wait")
       # 500 [Hz] 75% (neutral)
        pi.hardware_PWM(gpio_pin, 500, 750000)
        time.sleep(duration)
        pi.set_mode(gpio_pin, pigpio.INPUT)
        pi.stop()

def gripper_subscriber():
    rospy.init_node('gripper_subscriber', anonymous=True)
    rospy.Subscriber('gripper/pwm', Int64, callback)
    #rospy.Subscriber('gripper/pwm', Twist, callback)

    rospy.spin()

if __name__ == '__main__':
    gripper_subscriber()
