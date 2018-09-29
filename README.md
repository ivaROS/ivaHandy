# ivaHandy
document and code for Handy arm include tutorials, mechanical files and ROS-related packages.

## Doc
Doc includes tutorials about how to build your own robot arm. Contents contain the whole process starting from 
how to do assembly in Solidworks in order to  make urdf generation easier to use MoveIt! setup assitant to build 
your own robot arm MoveIt! package. 

## mechanical
mechanical includes 3DParts and Assembly two folders. 3DParts folder maintains all the files including Solidworks file, 
3Dprinting file and drawing that belong to individual piece.

## ros
ros folder keeps all ROS-related packages to the handy arm, which includes description, control, gazebo and MoveIt! package.
There are two verisons of Handy, one is the normal model which the other one is mesh-simplified model. Each has the four above packages.

### how to do motion planning in the real world for Handy
```
1. roslaunch finalarm_cotrol controller_manager.launch
2. roslaunch finalarm_control start_controller.launch
3. roslaunch finalarm_description robot_state_pub.launch
4. roslaunch finalarm_moveit_config move_group.launch
5. roslaunch finalarm_moveit_config moveit_rviz.launch
6. launch the file you write for Handy to do something like picking object, i.e. roslaunch handy_experiment pick.launch
```
