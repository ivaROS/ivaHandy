FROM ros:kinetic-ros-core-xenial

ENV ROS_PYTHON_VERSION=2

RUN apt-get update && \
    apt-get install -y \
        apt-utils \
        build-essential \
        git

# initalize rosdep
RUN rosdep init && rosdep update

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
COPY bin/ros_entrypoint.sh ./
ADD . src/ivaHandy
RUN rosdep install --from-paths src --ignore-src -r -y
RUN /app/ros_entrypoint.sh catkin_make

ENTRYPOINT ["/app/ros_entrypoint.sh"]