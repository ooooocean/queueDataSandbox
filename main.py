class Queue:
    # constructor
    def __init__(self, cap):
        self.queue = []
        self.cap = cap
        self.front = -1
        self.rear = -1
        self.arr = [0] * cap

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # creates queue
    def create_queue(self):
        return Queue(self.cap)