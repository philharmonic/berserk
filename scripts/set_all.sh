#!/bin/bash

# Usage: e.g.
# ./set_all 800Mhz


echo "Set all cores to $1"

# get num. of cores
CORES=`lscpu -p | grep ^[^#] | wc -l`

# configure each core
for num in $(eval echo {0..$[CORES-1]}); do
    sudo cpufreq-set -f $1 -c$num
done

cpufreq-info  | grep "available frequency steps"

cpufreq-info | grep "current CPU frequency is"

echo "Done."

exit
