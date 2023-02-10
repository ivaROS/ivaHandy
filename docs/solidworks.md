# solidworks


## solidworks assembly

When assembling the arm in Solidworks, try to assemble the parts into different links.
For example, if your arm has 7 DOF which means it has 8 links, you need first get 8 sub-assemblies and then assemble them into the final arm assembly.

The mate between the nearby two links should be one concentric and one coincident.


## assembly to urdf

ROS has developed Solidworks add-in tool for automatical conversion from Solidworks assembly to urdf package.
Here is the link: http://wiki.ros.org/sw_urdf_exporter

There are still a lot of bugs during the process of conversion, here are some tips:

At the beginning, don't manually choose any axis, coordinate or joint type during configuration, just fill in the name of link and joint and choose the part belonged to this link. After build the whole tree of link, press export and it will automatically generate the coordinate and axis.
The joint axis should be correct if the mate is set correctly.

After automatical generation, usually the world coordinate is totally wrong, you can manually set up all coordinates.
If you don't know how to choose the coordinate, you may refer some commercial robot arms like pr2.
In order to have a end effector link, you can set up a coordinate for it and add your eef link to be child of the wrist link.
Remember the joint type between eef link and wrist link should be fixed.
The eef link just helps you conveniently do eef pose computation.
You don't need to always compensate the length of the gripper.

After coordinate is done, go back to the UI of configuration, fill in the coordinate, axis and joint type and export the configuration.
In the post-configuration menu, you can fill in the low and high limit of your joint if you choose your joint type to be revolute.
Remember the automatically generated inertial moments of link are wrong.
You should use Solidworks to get the correct inertial moments of each link relative to your coordinate.
Some mass center and mass can also be wrong.
But make sure that you can't change these parameters in the post-configuration menu.
You'd better change them directly in the urdf file.
Otherwise I assume it will affect the generation of mesh file which finally leads to the unstable of arm model in gazebo.
If you don't need to load the model in gazebo, inertial moments are irelevant to you.

When you create moveit package for your arm model and let it go somewhere, you may find some joints rotate the opposite way.
You just need to flip the joint axis in urdf file and it is fine.

## using the urdf in gazebo

The problem you may meet when load arm model in gazebo is arm is unstable and keeps shaking.
Even worst, it may explode link by link.
In order to make your arm stable in gazebo and implement control for it, here are some tips:

Firstly, turn collision and gravity off to make sure the passive behavior of your arm is correct.
Basically, the inertial moments should be the one needed modification if you generate your urdf from Solidworks.
Then add `<dynamics damping="0.5"/>` tag to each joint tag.
And the effort and velocity tag in joint limit are all zero when generated, you need to set it to a certain value.
If the arm is still unstable after the inertial moments are corrected, you can try to add tag `<implicitSpringDamper>True</implicitSpringDamper>` to each joint.
It may help.
Here is the official tutorial from gazebo, http://gazebosim.org/tutorials/?tut=ros_urdf.

2After the passive behavior of arm is correct, you are close to success and just need to implement ros control.
Here is the official tutorial from gazebo, http://gazebosim.org/tutorials/?tut=ros_control.
My suggesstion is to go through tutorial and find some examples to follow.
There may be some small problems caused by ros version.
When you meet it, just google it and you will find solution.
