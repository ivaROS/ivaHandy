# generating moveit package

Generation of moveit configuration package can be divided into two parts.
One is use moveit setup assistant to configurate your arm and the other is to modify some files within the automatically generated package.

I will just mention the key points, the rest steps you can follow the official tutorial from MoveIt!.
First you need to create group for your robot arm. Here we have two groups.
The first one is arm group and the other one is end effector group.
For the arm group, you just need setup chain for it.
Chain should starts from the root to the end effector.
For the end effector group, add links of your end effector link and two links belonged to your gripper and joints belonged to your gripper.
Secondly when configurate end effector, choose parent link to be your the end effector link and group to be your end effector group.

1. Add controllers.yaml in config folder
1. Modify finalarm_description_moveit_controller_manager.launch.xml file
1. Change the default argument of config in moveit_rviz.launch to true
1. Optional: you can turn animation loop off in `trajectory_execution.launch.xml`: `<param name="trajectory_execution/execution_duration_monitoring" value="false" />`
