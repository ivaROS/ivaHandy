FROM ros:kinetic-ros-core-xenial

ENV ROS_PYTHON_VERSION=2

RUN apt-get update && \
    apt-get install -y \
        apt-utils \
        build-essential \
        git

# use the following command in a running container to find dependencies that we
# can install ahead of time
#
#   rosdep install --from-paths src --ignore-src -r -y --simulate --reinstall
RUN apt-get install -y \
    ros-kinetic-moveit-simple-controller-manager \
    gazebo7 \
    python-serial

# Initalize rosdep; note that kinetic is EOL so we need to include the following
# flag. If we leave it out, we will miss installing important dependencies.
RUN rosdep init && rosdep update --include-eol-distros

WORKDIR /app
# we add in our dependencies before building, to reduce future build steps
RUN mkdir src
RUN cd src && git clone https://github.com/ivaROS/ivaDynamixel.git
# pull any dependencies needed by the workspace
RUN rosdep install --from-paths src --ignore-src -r -y

# create the initial project using the system ros
# NOTE: the src/ directory needs to exist at the initial make
RUN /ros_entrypoint.sh catkin_make

# copy in our own entrypoint
ADD bin ./bin
ADD . src/ivaHandy
RUN rosdep install --from-paths src --ignore-src -r -y
RUN /app/bin/ros_entrypoint.sh catkin_make

ENTRYPOINT ["/app/bin/ros_entrypoint.sh"]