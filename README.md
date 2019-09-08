# GPIO_output package
This is **a ROS wrapper** for BlueRobotics Screw, Gripper and Sonar.

![](rosgraph.png)

In addition, this package assumes connecting a screw and gripper to *Rasberry Pi GPIO*, and snonar to USB.
Please refer to the following sites for parts installation and circuit wiring.

- Screw (use 13pin)
  - https://bluerobotics.com/store/thrusters/t200-thruster/

- Gripper (use 18pin)
  - https://bluerobotics.com/store/rov/bluerov2/newton-gripper-asm-r1-rp/

- Sonar (use USBserial port)
  - https://bluerobotics.com/store/sensors-sonars-cameras/sonar/ping-sonar-r2-rp/
  - https://github.com/bluerobotics/ping-python

# How to use it (ROS set up)
## Step0 : ssh conection to Rasberrypi.
```sh
$ ssh pi@ip_adress_of_your_raspi
type passward
```
## Step1 : change directory and gitclone this repository．
```sh
$ cd ~/your_ws/src
$ gitclone https://github.com/kumahika/GPIO_output
```
## Step3 : build(In the case of 'catkin_make')
```sh
$ cd ~/your_ws/
$ catkin_make
```
## Step4 : Grant execute permission
```sh
$ cd ~/your_ws/src/GPIO_output/src
$ chmod +x screw_sub.py
$ chmod +x gripper.py
$ chmod +x sonar_pub.py
```
## Step5 : Run a screw node if the build is successful. 
```sh
$ cd ~/your_ws/
$ source devel/setup.bash
$ rosrun GPIO_output screw_sub.py
```
## Step6 : Run multi nodes using roslaunch.
```sh
$ roslaunch GPIO_output act3.launch
```
## Step7 debug
Check all topics 
```sh
$ rostopic list
/gripper/pwm
/rosout
/rosout_agg
/screw/pwm
/sonar/confidence
/sonar/distance
/sonar/ping_interval
/sonar/ping_number
/sonar/scan_length
/sonar/scan_start
/sonar/speed_of_sound
/sonar/transmit_duration
/sonar/voltage
```
Screw operation test
```sh
$ rostopic pub /screw/pwm Int64 -- '3'
ON OF
mid
```
Gripper operation test
```sh
$ rostopic pub /gripper/pwm Int64 -- '3'
Open and Close
mid
```

# Rosparam setting
You can set up pwm duty and duration of screw and gripper.
Execute the following code or specify options in the launch file.
```sh
$ rosparam set /duration_screw '2' # unit is sec
$ rosparam set /duration_gripper '2' # unit is sec
$ rosparam set /pwm_screw '100' # You can set duty between -100 and 100.
```
