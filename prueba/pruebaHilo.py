import select
import threading
import time


class StoppableThread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self):
        super(StoppableThread, self).__init__()
        self._stop = threading.Event()

    def run(self):
        while not self.stopped():
            print("name:{}".format(self.name))
            time.sleep(0.8)

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()


if __name__ == '__main__':
    t1 = StoppableThread()
    t2 = StoppableThread()
    try:
        t1.daemon = True
        t1.start()
        while 1:
            select.select([], [], [])
    except (KeyboardInterrupt, SystemExit):
        t1.stop()