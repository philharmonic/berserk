# General
# ---------
# how long to run the benchmark
# hh:mm:ss
# max 23:59:59
duration = "00:00:04"
#duration = "23:59:59"
auto_duration=True
# if False, you have to manually specify:
tasks = 3
# single task complexity (e.g. n for Fibonacci) 
task_size = 30


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

# Benchmark estimation details
#-------------------------------

# the desired length of a single task
period = 1 # seconds

# number of repeats to get the estimated period
repeats = 5


# I/O-bound benchmark settings
#-----------------------------

berserk_server_domain = 'localhost'
berserk_server_port = 8089
berserk_server_url = 'http://{}:{}/'.format(
    berserk_server_domain, berserk_server_port
)
