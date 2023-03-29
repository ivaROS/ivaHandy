cmake_minimum_required(VERSION 2.8.3)

project(finalarm_description)

find_package(catkin REQUIRED COMPONENTS xacro)

catkin_package()

find_package(roslaunch)

# build urdf files into the share directory for backwards compatibility
file(GLOB xacro_files urdf/*.urdf.xacro)
xacro_add_files(${xacro_files} INSTALL DESTINATION urdf)

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
