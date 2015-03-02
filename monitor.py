"""A background process to monitor CPU usage."""

from queue import Empty
from multiprocessing import Process, Queue
from log import log_client as log
#import time

import psutil
import pandas as pd

class Monitor(Process):

    def __init__(self):
        super(Monitor, self).__init__()
        self.queue = Queue()
        self.measurements = []
        self.times = []

    def _take_measurement(self):
        util = psutil.cpu_percent(interval=1, percpu=True)
        util = {core: util for core, util in enumerate(util)}
        t = pd.datetime.now()
        self.measurements.append(util)
        self.times.append(t)

    def _finalize(self):
        self.util = pd.DataFrame(self.measurements, self.times)
        self.util.to_csv('measurements.csv')
        log('Mean CPU utilisation: {}'.format(self.util.mean().mean()))

    def run(self):
        while True:
            try:
                cmd = self.queue.get(block=False)
                if cmd == 'quit':
                    break
            except Empty:
                #time.sleep(1)
                self._take_measurement()
        self._finalize()
        self.queue.put('done')
