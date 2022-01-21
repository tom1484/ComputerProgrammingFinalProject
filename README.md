# Team9_code

## main_project

**requirements:  Testing should be done on RPi**.

All files under this folder are located in  `~/catkin_ws/src/project ` .

Since there are some bugs of **Kimera**, it can not publish 3D-mesh in mono-camera mode, Therefore, there are options options to test the project: 

* **Test with local hardware inputs**

  ``` shell
  # The following commands have to be executed in different terminal.
  
  # start publshers of hardware data and simulation clock
  roslaunch project publish.launch
  
  # start Kimera-VIO in mono mode
  roslaunch roslaunch kimera_vio_ros kimera_vio_ros_eurocmono.launch
  
  # visualizing Kimera output
  rviz -d ~/catkin_ws/src/Kimera-VIO-ROS/rviz/kimera_vio_euroc.rviz
  ```

* **Test with official dataset**

  ```shell
  # The following commands have to be executed in different terminal.
  
  # start playing dataset
  rosbag play --clock ~/catkin_ws/data/V1_01_easy.bag
  # start Kimera-VIO in stereo mode
  roslaunch roslaunch kimera_vio_ros kimera_vio_ros_euroc.launch online:=true
  
  # start analyzing of mesh
  rosrun project mesh_analysis.py
  
  # visualizing Kimera output
  rviz -d ~/catkin_ws/src/Kimera-VIO-ROS/rviz/kimera_vio_euroc.rviz
  ```

To see the data published, you can run `rostopic echo <topic>` .  The corresponding topic of different type of data are:

| Topic                  | Content                                       |
| :--------------------- | --------------------------------------------- |
| `/imu0`                | accelerometer and gyro                        |
| `/cam0/image_raw`      | image from left camera                        |
| `/cam1/image_raw`      | image from right camera (only in stereo mode) |
| `/kimera_vio_ros/mesh` | 3D mesh from **Kimera** (only in stereo mode) |

## calibration

This folder contains codes for calibrating camera and MPU6050.

### camera_calibration

**requirements:**  Install `requirements.txt` 

Run one of the following

```shell
python calibration.py
python3 calibration.py
```

### MPU6050_calibration

**requirements:**  Install `MPU6050` in `Library Manager` 

Connect `SDA`, `SCL` on Arduino, upload sketch, open `Serial Monitor`, and set baud rate to 38400.

