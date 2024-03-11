class Queue:
    # constructor
    def __init__(self, cap):
        self.cap = cap
        self.front = 0
        self.rear = 0
        self.queue = [0] * cap

    def is_full(self):
        return bool(self.rear == self.cap)


    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # initialises empty queue
    def create_queue(self):
        return Queue(self.cap)
