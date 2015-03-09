#!/bin/bash


echo "Info on all cores."

cpufreq-info | grep "current CPU frequency is"

exit
