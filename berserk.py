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

def cpu():
    a = 0.8*2.3
    
def finalize(results):
    benchmark_notifier.notify_master(host=conf.host, data=results)

def run_from_conf(conf):
    logging.basicConfig(filename='berserk.log',
                        level=logging.DEBUG,
                        format='%(asctime)s %(message)s')
    #memory(size=conf.size)
    if conf.method=="memory":
        import memory
        size_mb = conf.size
        run_period = conf.run_period
        memory.run(size_mb, run_period)
    elif conf.method=="time":
        # get an estimate of the task complexity on this hardware
        log("------------------\nBERSERK BENCHMARK\n------------------")
        import fibonacci as fib
        log("Looking for %d s Fibonacci job." % (conf.run_period))
        n, interval = fib.find_time(conf.run_period)
        log("Found 1st longer calculation (t = %d) and it's for n = %d." % (interval, n))
        # parse run_time
        t = datetime.strptime(conf.run_time,"%H:%M:%S")
        delta = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
        run_time = delta.total_seconds()
        log("We want to run a job for %s (%d s)." % (str(delta), run_time))
        # adapt the number of runs
        run_num = int(math.ceil(run_time/float(interval)))
        # run the job
        estimation = timedelta(seconds = run_num*interval)
        log("Doing %d runs of %dth Fibonacci number calculation" % (run_num, n))
        log("#estimation %s." % (str(estimation)))
        t1 = time()#TODO: get rid of time, using datetime for runs lasting multiple days
        dt1 = datetime.now()
        log("#start %s" % (str(dt1)))
        for i in range(run_num):
            fib.fibonacci(n)
        t2 = time()
        dt2 = datetime.now()
        log("#end %s" % (str(dt2)))
        duration = t2-t1
        log("Finished. It took: %.2f s (%.2f min)" % (duration, (duration)/60.))
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
