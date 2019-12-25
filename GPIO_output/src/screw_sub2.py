#!/usr/bin/env python

import pigpio
import time
import rospy
from std_msgs.msg import Int64

def callback(msg):
    global duty
    control_flag = msg.data
    # gpio_pin = 13
    # norm_pwm = rospy.get_param('~pwm_screw')
    # duty = (250 * norm_pwm) + 750000
    # print("duty%d" % duty)
    # duration = rospy.get_param('~duration_screw')
    # pi = pigpio.pi()
    # pi.set_mode(gpio_pin, pigpio.OUTPUT)
    # pi.hardware_PWM(gpio_pin, 500, 750000)
    # time.sleep(duration)
    if control_flag == 1 and duty < 850000:
        # 500 [Hz] 75% (pwm 1500) 
        duty += step
        print("increment, duty=%d" % duty)
        #pi.set_mode(gpio_pin, pigpio.OUTPUT)
        #pi.hardware_PWM(gpio_pin, 500, duty)
        #time.sleep(duration)
        #pi.set_mode(gpio_pin, pigpio.INPUT)
        #pi.stop()
    elif control_flag == 2 and duty > 650000:
        duty -= step
        print("decrement, duty=%d" % duty)
    elif control_flag == 0:
        print("OFF")
        #500 [Hz] 75% (neutral)
        #pi.set_mode(gpio_pin, pigpio.OUTPUT)
        #pi.hardware_PWM(gpio_pin, 500, 750000)
        #time.sleep(duration)
        duty = 750000
    pi.hardware_PWM(gpio_pin, 500, duty)

def screw_subscriber():
    rospy.init_node('screw_subscriber', anonymous=True)
    rospy.Subscriber('screw/pwm', Int64, callback)
    rospy.spin()

if __name__ == '__main__':
    global duty
    gpio_pin = 13
    norm_pwm = 55
    step = 10000/2
    duty =  750000 + (0.4*norm_pwm-20)*10000
    print("duty%d" % duty)
    duration = 0.1
    pi = pigpio.pi()
    pi.set_mode(gpio_pin, pigpio.OUTPUT)
    pi.hardware_PWM(gpio_pin, 500, 750000)
    time.sleep(duration)
    screw_subscriber()
