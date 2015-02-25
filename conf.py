# General
# ---------
# how long to run the benchmark
# hh:mm:ss
# max 23:59:59
duration = "00:00:04"
#duration = "23:59:59"
auto_duration=True
# if False, you have to manually specify:
tasks = 60
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

#berserk_server_domain = 'localhost'
berserk_server_domain = 'happy'
berserk_server_port = 8089
berserk_server_url = 'http://{}:{}/'.format(
    berserk_server_domain, berserk_server_port
)

# the ratio of tasks to perform remotely on the server
remote_task_ratio = 0.2

# the number of rounds that local/remote execution is switched
# e.g.
# - tasks = 30
# - remote_task_ratio = 0.3
# - local_remote_rounds = 1 -> 10 remote, 20 local
# - local_remote_rounds = 2 -> 5 remote, 10 local, 5 remote, 10 local
# local_remote_rounds = 2
local_remote_rounds = tasks / 10
