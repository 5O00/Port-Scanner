import threading
import queue


class Worker(threading.Thread):
    def __init__(target, ip, queue, out_queue):
        self.target = target
        self.ip = ip
        self.queue = queue
        self.out_queue = out_queue

    def run(self):
        while not queue.isempty():
            port = queue.get()

            if self.target(self.ip, port):
                out_queue.append(port)