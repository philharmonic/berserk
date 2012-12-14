'''
Created on Dec 13, 2012

@author: kermit
'''
import conf
from berserk import cpu, memory
from fibonacci import fibonacci

def log(something):
    print(something)
    
def _find_job_size_for_period(job, period):
    """
    finds first job size that is longer than the period
    @param period: 
    """
    measured = 0
    n = 0
    while(measured < period):
        n+=1
        t1 = time.time()
        fibonacci(n)
        t2 = time.time()
        measured = t2-t1

def time_cpu():
    # get an estimate of the task complexity on this hardware
    log("Looking for %d s Fibonacci job." % (conf.run_period))
    n, interval = fib.find_time(conf.run_period)
    _find_job_size_for_period(job=fibonacci)
    log("Found 1st longer calculation (t = %d) and it's for n = %d." % (interval, n))
    # parse duration
    t = datetime.strptime(conf.duration,"%H:%M:%S")
    delta = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
    duration = delta.total_seconds()
    log("We want to run a job for %s (%d s)." % (str(delta), duration))
    # adapt the number of runs
    run_num = int(math.ceil(duration/float(interval)))
    # run the job
    estimation = timedelta(seconds = run_num*interval)
    log("#estimation %s." % (str(estimation)))
    
def measure(method):
    if method=="cpu":
        time_cpu()
        
def estimate_run():
    pass

def plan_benchmark(desired_time, method):
    #warm_up()
    measure(method)
    estimate_run()

if __name__ == '__main__':
    plan_benchmark()