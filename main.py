class Queue:
    # constructor
    def __init__(self, cap):
        self.cap = cap-1
        self.front = -1
        self.rear = -1
        self.queue = [0] * cap

    def is_full(self):
        return bool(self.rear == self.cap)

    def is_empty(self):
        return bool(self.front == -1 and self.rear == -1)

    def enqueue(self, item):
        # throw overflow error if the queue is full
        if self.is_full():
            print('Queue is full.')
            return
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print('Queue is empty.')
            return


    # initialises empty queue
    def create_queue(self):
        return Queue(self.cap)
