from datetime import datetime
import concurrent.futures
import pickle

from log import log

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

def cpu(run_num, n):
    import fibonacci as fib
    log("Doing {} runs of {}th Fibonacci num. calculation.".format(run_num, n))
    # a process worker will be generated for every core by default
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # we map all the tasks over the process pool
        for result in executor.map(fib.fibonacci, (n for i in range(run_num))):
            # collect the results by iterating over the map (no timeout)
            pass # optionally do sth with the result
    # old single-core version
    # for i in range(run_num):
    #     fib.fibonacci(n)

def finalize(results):
    with open("io/results.pkl", "wb") as results_pkl:
        pickle.dump(results, results_pkl)
    import benchmark_notifier
    benchmark_notifier.notify_master(host=conf.host, data=results)

def run_from_conf(conf):
    if conf.auto_duration:
        from plan_benchmark import plan_benchmark
        tasks, task_size = plan_benchmark(conf.duration, conf.method)
    else:
        tasks, task_size = conf.tasks, conf.task_size

    log("------------------\nBERSERK BENCHMARK\n------------------")
    dt1 = datetime.now()
    log("#start %s" % (str(dt1)))

    if conf.method=="memory":# TODO: fix this
        size_mb = conf.size
        run_period = conf.run_period
        memory(size_mb, run_period)
    elif conf.method=="cpu":
        cpu(tasks, task_size)

    dt2 = datetime.now()
    log("#end %s" % (str(dt2)))
    dt_runtime = dt2-dt1
    log("#runtime %s (%d s)" % (str(dt_runtime), dt_runtime.seconds))
    #results = {"dt_runtime": dt_runtime, "runtime": duration}
    results = (dt1, dt2)
    try:
        finalize(results)
    except Exception as e:
        log("Warning: Can't notify benchmark master. {}".format(str(e)))
    log("\n------------------\n")

def sample_run():
    while True:
        #memory()
        cpu()

if __name__ == "__main__":
    #sample_run()
    import conf
    run_from_conf(conf)
