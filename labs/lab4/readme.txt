roscore
rosrun turtlesim turtlesim_node
rosrun turtlesim turtle_teleop_key

Task2
rosservice call /spawn 3.0 3.0 0.0 'turtle702'
name: "turtle702"

rosbag record -a -O cmd_record_1155159702

rostopic list -v


catkin_make
echo $ROS_PACKAGE_PATH
source devel/setup.bash
roscd beginner_tutorial

# catkin_create_pkg <package_name> [depend1] [depend2] [depend3]
$ cd ~/catkin_ws/src
$ catkin_create_pkg beginner_tutorials std_msgs rospy roscpp

rosrun turtlesim turtlesim_node
rosrun turtlesim turtle_teleop_key

rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist "linear:
  x: 0.0
  y: 0.0
  z: 0.0
angular:
  x: 0.0
  y: 0.0
  z: 0.0"
