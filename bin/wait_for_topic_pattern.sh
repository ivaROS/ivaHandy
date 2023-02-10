#!/usr/bin/env bash
set -e

# wait NUM_RETRY times until a topic with a grep pattern appears

num_retry=${NUM_RETRY:-15}
for i in $(seq 1 $num_retry); do
    rostopic list | grep "$1" && break || sleep 1
    echo "retry $i"
done
