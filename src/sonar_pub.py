#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64

from brping import Ping1D
import time
import argparse

from builtins import input

def sonar_publisher():
    #parser = argparse.ArgumentParser(description="Ping python library example.")
    #parser.add_argument('--device', action="store", required=True, type=str, help="Ping device port.")
    #parser.add_argument('--baudrate', action="store", type=int, default=115200, help="Ping device baudrate.")
    #args = parser.parse_args()
    #Make a new Ping
    #myPing = Ping1D(args.device, args.baudrate)
    myPing = Ping1D("/dev/ttyUSB0", 115200)
    if myPing.initialize() is False:
        print("Failed to initialize Ping!")
        exit(1)
    #input("Press Enter to continue...")

    pub_dis = rospy.Publisher('sonar/distance', Int64, queue_size=10)
    pub_conf = rospy.Publisher('sonar/confidence', Int64, queue_size=10)
    pub_trans_dura = rospy.Publisher('sonar/transmit_duration', Int64, queue_size=10)
    pub_ping_num = rospy.Publisher('sonar/ping_number', Int64, queue_size=10)
    pub_scan_start = rospy.Publisher('sonar/scan_start', Int64, queue_size=10)
    pub_scan_length = rospy.Publisher('sonar/scan_length', Int64, queue_size=10)
   # pub_gain_setting = rospy.Publisher('sonar/gain_setting', Int64, queue_size=10)
    pub_speed_of_sound = rospy.Publisher('sonar/speed_of_sound', Int64, queue_size=10)
    pub_voltage = rospy.Publisher('sonar/voltage', Int64, queue_size=10)
    pub_ping_interval = rospy.Publisher('sonar/ping_interval', Int64, queue_size=10)

    rospy.init_node('sonar_publisher', anonymous=True)
    r = rospy.Rate(60)
    while not rospy.is_shutdown():
        data = myPing.get_distance()
        data2 = myPing.get_speed_of_sound()
        data3 = myPing.get_general_info()
        if data:
            print("Distance: %s\tConfidence: %s%%" % (data["distance"], data["confidence"]))
            #time.sleep(0.1)
            pub_dis.publish(data["distance"])
            pub_conf.publish(data["confidence"])
            pub_ping_num.publish(data["ping_number"])
            pub_scan_start.publish(data["scan_start"])
            pub_scan_length.publish(data["scan_length"])
            #pub_gain_setting.publish(data["gain_setting"])
        if data2:
            pub_speed_of_sound.publish(data2["speed_of_sound"])
        r.sleep()
        if data3:
            pub_voltage.publish(data3["voltage_5"])
            pub_voltage.publish(data3["ping_interval"])

if __name__ == '__main__':
    try:
        sonar_publisher()
    except rospy.ROSInterruptException: pass
