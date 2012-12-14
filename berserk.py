import math
from time import time
from datetime import datetime, timedelta
import logging
import benchmark_notifier

def log(something):
    print(something)
    logging.info(something)


# MEMORY
#---------------------
# import sys

# class Structure(object):
#     data = "abcd"
#     def __init__(self, l):
#         self.reserved = l*self.data

# def memory(size = 1):
#     """
#     @param size: MBs to allocate
#     """
#     # allocate
#     data = range(10000)
#     size = sys.getsizeof(data)
#     log("allocated %d bytes" % (size))
#     # read / write
#---------------------

def memory(size_mb,run_period):
    import memory
    memory.run(size_mb, run_period)

def cpu():
    a = 0.8*2.3
    
def finalize(results):
    log("------------------\n")
    benchmark_notifier.notify_master(host=conf.host, data=results)

def run_from_conf(conf): #TODO: run until datetime.now()==designated_time
    logging.basicConfig(filename='berserk.log',
                        level=logging.DEBUG,
                        format='%(asctime)s %(message)s')
    if conf.method=="memory":
        size_mb = conf.size
        run_period = conf.run_period
        memory(size_mb, run_period)
    elif conf.method=="cpu":
        cpu()
    elif conf.method=="cpu":
        log("------------------\nBERSERK BENCHMARK\n------------------")
        import fibonacci as fib
        if conf.auto_duration:
            # get an estimate of the task complexity on this hardware
            log("Looking for %d s Fibonacci job." % (conf.run_period))
            n, interval = fib.find_time(conf.run_period)
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
        else:
            log("Manually set no. of iterations and N")
            run_num = conf.iterations
            n = conf.n
        log("Doing %d runs of %dth Fibonacci number calculation" % (run_num, n))
        dt1 = datetime.now()
        log("#start %s" % (str(dt1)))
        for i in range(run_num):
            fib.fibonacci(n)
        dt2 = datetime.now()
        log("#end %s" % (str(dt2)))
        dt_runtime = dt2-dt1
        log("#runtime %s (%d s)" % (str(dt_runtime), dt_runtime.seconds))
        #results = {"dt_runtime": dt_runtime, "runtime": duration}
        results = (dt1, dt2)
        try:
            finalize(results)
        except:
            log("Warning: Can't notify the benchmark master of the outcome.")
    
def sample_run():
    while True:
        #memory()
        cpu()

if __name__ == "__main__":
    #sample_run()
    import conf
    run_from_conf(conf)
