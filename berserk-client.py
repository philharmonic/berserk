"""The client side of the I/O-bound Berserk benchmark"""

from datetime import datetime
import logging

import requests

from log import log_client as log
from berserk import finalize, cpu
from monitor import Monitor

def send_requests(tasks, task_size):
    if tasks == 0:
        return
    params = {'tasks': tasks, 'task_size': task_size}
    response = requests.get(conf.berserk_server_url, params=params)
    result = response.json()['result']
    return result

def run_from_conf(conf):
    # CPU monitoring
    mon = Monitor()
    mon.start()

    log("\n------------------\nBERSERK BENCHMARK\n------------------\n")
    dt1 = datetime.now()
    log("#start %s" % (str(dt1)))

    tasks, task_size = conf.tasks, conf.task_size
    tasks_remote = int(round(tasks * conf.remote_task_ratio))
    tasks_local =  tasks - tasks_remote

    done_tasks_local = 0
    done_tasks_remote = 0
    tasks_remote_round = int(round(tasks_remote /
                                   float(conf.local_remote_rounds)))
    tasks_local_round = int(round(tasks_local /
                                  float(conf.local_remote_rounds)))

    try:
        local_rounds = tasks_local / tasks_local_round
    except ZeroDivisionError:
        local_rounds = 0
    try:
        remote_rounds = tasks_remote / tasks_remote_round
    except ZeroDivisionError:
        remote_rounds = 0
    num = max(local_rounds, remote_rounds)
    log('Doing approx. {} interlaced local/remote rounds.'.format(num))

    # interlace local and remote tasks
    while done_tasks_local < tasks_local or done_tasks_remote < tasks_remote:
        # TODO: perform local and remote tasks in parallel
        # TODO: perform the CPU calculations in a process pool to use all cores
        # send requests to berserk-server and collect the results
        log('Sending {} remote tasks...'.format(tasks_remote_round))
        send_requests(tasks_remote_round, task_size)
        log("... Done.")
        done_tasks_remote += tasks_remote_round
        log('Doing {} local tasks'.format(tasks_local_round))
        cpu(tasks_local_round, task_size)
        done_tasks_local += tasks_local_round

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

    # stop monitoring
    mon.queue.put('quit')
    mon.join()

if __name__ == "__main__":
    import conf
    run_from_conf(conf)
