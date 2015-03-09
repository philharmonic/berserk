#!/bin/bash


# get num. of cores
CORES=`lscpu -p | grep ^[^#] | wc -l`

# configure each core
for num in $(eval echo {0..$[CORES-1]}); do
    echo "Setting core $num to ondemand."
    sudo cpufreq-set -g ondemand -c$num
done

echo "Back to ondemand. We're green."

exit
