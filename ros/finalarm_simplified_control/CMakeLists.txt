cmake_minimum_required(VERSION 2.8.3)
project(finalarm_simplified_control)

find_package(catkin REQUIRED)

catkin_package()

find_package(roslaunch)

install(DIRECTORY launch DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
install(DIRECTORY config DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
