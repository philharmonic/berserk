"""The client side of the I/O-bound Berserk benchmark"""

from datetime import datetime

import requests

from log import log
from berserk import finalize

def send_requests(conf):
    params = {'tasks': 3, 'task_size': 10}
    response = requests.get(conf.berserk_server_url, params=params)
    result = response.json()['result']
    log(result)

def run_from_conf(conf):
    log("------------------\nBERSERK BENCHMARK\n------------------")
    dt1 = datetime.now()
    log("#start %s" % (str(dt1)))

    # send requests to berserk-server and collect the results
    send_requests(conf)
    # TODO: combine local and remote tasks

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

if __name__ == "__main__":
    import conf
    run_from_conf(conf)
