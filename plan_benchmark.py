'''
Created on Dec 13, 2012

@author: kermit

If we want to run a benchmark for several hours or days, we have a small 
task:

 - calculation of the n-th Fibonacci number
 - sleeping while occupying memory
 ...

The benchmark then consists of many runs of this tasks

    benchmark = task * run_num
    
This module's goal is to try to plan a benchmark that will last for 
a desired time. This is done by first finding an appropriate task size
in the _find_task_size function and then using the time of running this 
single task -- the **period** and estimate the run_num of tasks 
that would make the whole benchmark's time at least the desired total time.
'''
import timeit
import numpy as np
import math
from datetime import datetime, timedelta

import conf
from log import log
    
def _find_task_size(method, desired_period):
    """
    Get an estimate of the task complexity on this hardware.
    Finds first job size that lasts longer than the desired_period
    @param desired_period: float seconds 
    """
    t = 0
    size = 0
    log("Looking for a %d s task." % (desired_period))
    while t < desired_period:
        size += 1 
        timer = _get_timer(method, size)
        t = timer.timeit(1)
    log("Found 1st long-enough task (t = %f) and it's for n = %d." % (t, size))
    return size
    
def _get_timer(method="cpu", size=27):
    if method=="cpu":
        timer = timeit.Timer(stmt='fibonacci(%d)' % (size),
                            setup='from fibonacci import fibonacci')#; gc.enable()')
    return timer
    

def measure(method):
    """
    get the approx. 1-sec. task and time it
    in many runs to get an estimation of the
    required number of runs
    """
    size = _find_task_size(method, conf.period)
    repeats = conf.repeats
    timer = _get_timer(method, size)
    periods = timer.repeat(repeats, 1)
    periods = np.array(periods)
    print(periods)
    best_period = periods.min()
    print(best_period)
    return size, best_period
    
        
def estimate_run(benchmark_duration, period):
    run_num = int(math.ceil(benchmark_duration/float(period)))
    estimation = timedelta(seconds = run_num*period)
    log("#estimation %s." % (str(estimation)))
    return run_num, estimation

def plan_benchmark(benchmark_duration, method):
    # parse duration
    t = datetime.strptime(benchmark_duration,"%H:%M:%S")
    delta = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
    benchmark_duration = delta.total_seconds()
    log("We want to run a job for %s (%d s)." % (str(delta), benchmark_duration))
    # plan...
    task_size, period = measure(method)
    run_num, estimation = estimate_run(benchmark_duration, period)
    log("We estimate that doing %d tasks of size %d will last %s." 
        % (run_num, task_size, str(estimation)))
    return run_num, task_size

if __name__ == '__main__':
    plan_benchmark(conf.duration, conf.method)