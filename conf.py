# General
# ---------
# how long to run the benchmark
# hh:mm:ss
# max 23:59:59
duration = "00:00:03"
#duration = "23:59:59"
auto_duration=True
# if False, you have to manually specify:
iterations = 69723 
n = 30

#methods avaliable:
# - memory
# - time
method = "time"

# Memory consumption
#-------------------
run_period = 1 # seconds
#size to occupy
size = 300 # MB

# Host to notify with the results
#---------------------------------
host = 'http://localhost:8088/'
#host = 'http://snowwhite:8088/'
