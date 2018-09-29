# ivaHandy
document and code for Handy arm include tutorials, mechanical files and ROS-related packages.

## Doc
Doc includes tutorials about how to build your own robot arm. Contents contain the whole process starting from 
how to do assembly in Solidworks in order to  make urdf generation easier to use MoveIt! setup assitant to build 
your own robot arm MoveIt! package. 

## mechanical
mechanical includes 3DParts and Assembly two folders. 3DParts folder maintains all the files including Solidworks file, 
3Dprinting file and drawing that belong to individual piece. Assembly holds models for the whole arm and each link.

## ros
ros folder keeps all ROS-related packages to the handy arm, which includes description, control, gazebo and MoveIt! package.
There are two verisons of Handy, one is the normal model which the other one is mesh-simplified model. Each has the four above packages.

### Dependency
1. If you'd like to use finalarm_gazebo package, you should git clone balabala packages to your workspace since gazebo has dependencies on these packages if you want to load controllers in gazebo.

2. If you just need finalarm_conrtol, finalarm_description and finalarm_moveit_config packages, in order to compile all packages out, you additionally need a package named dynamixel_motor which applies designed controllers for dynamixel motors.

### How to do motion planning in the real world for Handy
 * The first step you need to launch controller manager which will start a node responsible for managing all loaded controllers

 * The second step is loading configuration for individual controller 

 * The third step is mainly starting nodes which will publish integrated information of all controllers and transformation information between each links 

 * The fourth step is to launch move_group node which does all motion planning, collision checking and etc jobs

 * The fifth step is to run rviz for visualization

 * The sixth step is to run code that you write for Handy to let it do things you want it to do
```
1. roslaunch finalarm_cotrol controller_manager.launch
2. roslaunch finalarm_control start_controller.launch
3. roslaunch finalarm_description robot_state_pub.launch
4. roslaunch finalarm_moveit_config move_group.launch
5. roslaunch finalarm_moveit_config moveit_rviz.launch
6. launch the file you write for Handy to do something like picking object, i.e. roslaunch handy_experiment pick.launch
```
