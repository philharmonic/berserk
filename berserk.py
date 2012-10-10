import math
from time import time

def log(something):
    print(something)


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

def run_from_conf(conf):
    #memory(size=conf.size)
    if conf.method=="memory":
        import memory
        size_mb = conf.size
        run_period = conf.run_period
        memory.run(size_mb, run_period)
    elif conf.method=="time":
        # get an estimate of the task complexity on this hardware
        import fibonacci as fib
        from datetime import datetime, timedelta
        log("Looking for a %d second Fibonacci job." % (conf.run_period))
        n, interval = fib.find_time(conf.run_period)
        # parse run_time
        t = datetime.strptime(conf.run_time,"%H:%M:%S")
        delta = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
        run_time = delta.seconds
        log("We want to run sth for %d seconds." % (run_time))
        # adapt the number of runs
        run_num = int(math.ceil(run_time/float(interval)))
        # run the job
        log("Doing %d runs of %dth Fibonacci number." % (run_num, n))
        t1 = time()
        for i in range(run_num):
            fib.fibonacci(n)
        t2 = time()
        duration = t2-t1
        print("Finished. It took: %.2f s (%.2f min)" % (duration, (duration)/60.))
    
def sample_run():
    while True:
        memory()
        cpu()

if __name__ == "__main__":
    #sample_run()
    import conf
    run_from_conf(conf)
