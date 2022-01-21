# Team9_code

## main_project

All files under this folder are located in  `~/catkin_ws/src/project ` .

Since there are some bugs of **Kimera**, it can not publish 3D-mesh in mono-camera mode, Therefore, there are several options to test the project: 

* **Test with local hardware inputs**

  ``` shell
  # The following commands have to be executed in different terminal.
  
  # start publshers of hardware data and simulation clock
  roslaunch project publish.launch
  # start Kimera-VIO in mono-camera mode
  roslaunch roslaunch kimera_vio_ros kimera_vio_ros_eurocmono.launch
  # visualizing Kimera output
  rviz -d ~/catkin_ws/src/Kimera-VIO-ROS/rviz/kimera_vio_euroc.rviz
  ```

  H

* **Test with official dataset**

  ```shell
  # The following commands have to be executed in different terminal.
  
  # start publshers of hardware data and simulation clock
  roslaunch project publish.launch
  # start analyzing of mesh
  rosrun project mesh_analysis.py
  # start Kimera-VIO in mono-camera mode
  roslaunch roslaunch kimera_vio_ros kimera_vio_ros_euroc.launch online:=true
  # visualizing Kimera output
  rviz -d ~/catkin_ws/src/Kimera-VIO-ROS/rviz/kimera_vio_euroc.rviz
  ```

  H