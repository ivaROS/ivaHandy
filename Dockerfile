FROM ros:kinetic-ros-core-xenial

RUN apt-get update && \
    apt-get install -y \
        build-essential

WORKDIR /app
# create the initial project using the system ros depends
RUN mkdir src && /ros_entrypoint.sh catkin_make

# copy in our own entrypoint
COPY bin/ros_entrypoint.sh ./
ADD . src/ivaHandy
RUN /app/ros_entrypoint.sh catkin_make

ENTRYPOINT ["/app/ros_entrypoint.sh"]