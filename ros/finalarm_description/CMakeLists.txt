cmake_minimum_required(VERSION 2.8.3)

project(finalarm_description)

find_package(catkin REQUIRED COMPONENTS xacro)

catkin_package()

find_package(roslaunch)

# use relative paths
# file(GLOB xacro_files urdf/*.urdf.xacro)
# xacro_add_files(${xacro_files} TARGET urdf)

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
