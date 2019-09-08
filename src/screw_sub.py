#!/usr/bin/env python

import pigpio
import time
import rospy
from std_msgs.msg import Int64


def callback(msg):
    gpio_pin = 13
    control_flag = msg.data
    norm_pwm = rospy.get_param('/pwm_screw')
    duty = (250 * norm_pwm) + 750000
    print("duty%d" % duty)
    duration = rospy.get_param('/duration_screw')
    pi = pigpio.pi()
    pi.set_mode(gpio_pin, pigpio.OUTPUT)
    pi.hardware_PWM(gpio_pin, 500, 750000)
    time.sleep(duration)

    if control_flag == 1:
        # 500 [Hz] 75% (pwm 1500)
        print("ON")
        pi.hardware_PWM(gpio_pin, 500, duty)
        time.sleep(duration)
        pi.set_mode(gpio_pin, pigpio.INPUT)
        pi.stop()

    elif control_flag == 2:
        # 500 [Hz] 77.5% (pwm 1550: spin cw)
        print("OFF")
        pi.hardware_PWM(gpio_pin, 500, 750000)
        time.sleep(duration)
        pi.set_mode(gpio_pin, pigpio.INPUT)
        pi.stop()

     elif control_flag == 3:
        print("ON OFF")
        pi.hardware_PWM(gpio_pin, 500, duty)
        time.sleep(duration)
        print("mid")
        pi.hardware_PWM(gpio_pin, 500, 750000)
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

def screw_subscriber():
    rospy.init_node('screw_subscriber', anonymous=True)
    rospy.Subscriber('screw/pwm', Int64, callback)

    rospy.spin()

if __name__ == '__main__':
    screw_subscriber()
