# General
# ---------
# how long to run the benchmark
# hh:mm:ss
# max 23:59:59
duration = "00:00:03"
#duration = "23:59:59"
auto_duration=True
# if False, you have to manually specify:
iterations = 3
# single job complexity (e.g. n for Fibonacci) 
iteration_size = 30
# the approx. length of a single run cycle
run_period = 1 # seconds

#methods avaliable:
# - memory
# - cpu
method = "cpu"

# Memory consumption
#-------------------

#size to occupy
size = 300 # MB

# Host to notify with the results
#---------------------------------
host = 'http://localhost:8088/'
#host = 'http://snowwhite:8088/'
