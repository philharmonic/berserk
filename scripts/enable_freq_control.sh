#!/bin/bash

dpkg -s cpufrequtils 2>/dev/null >/dev/null || sudo apt-get -y install cpufrequtils

cpufreq-info | grep "available frequency steps"

# get num. of cores
CORES=`lscpu -p | grep ^[^#] | wc -l`

# configure each core
for num in $(eval echo {0..$[CORES-1]}); do
    echo "Setting core $num to userspace."
    sudo cpufreq-set -g userspace -c$num
done

echo "Set cores to userspace. We control the frequency manually."

exit