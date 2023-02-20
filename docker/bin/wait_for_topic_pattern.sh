#!/usr/bin/env bash
set -e

# wait NUM_RETRY times until a topic with a grep pattern appears

num_retry=${NUM_RETRY:-20}
sleep_sec=${SLEEP_SEC:-5}
for i in $(seq 1 $num_retry); do
    rostopic list | grep "$1" && exit 0 || sleep $sleep_sec
    echo "retry $i, sleeping $sleep_sec"
done

# we fell through, so lets exit with a different error code
exit 1
