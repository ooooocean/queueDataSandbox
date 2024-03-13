class Queue:
    # constructor
    def __init__(self, array=None, cap=None):
        if array is None and cap is None:
            print('Please specify either array or cap.')
            return
        if cap is not None:
            self.cap = (cap - 1)
            if array is not None:
                self.cap = len(array - 1)
        self.front = -1
        self.rear = -1
        if cap is not None:
            self.queue = [None] * cap
        if array is not None:
            self.queue = array
            self.cap = (len(array))
            for index, ele in enumerate(array):
                if ele is None and self.front == -1:
                    self.front = index
                if ele is None and self.rear == -1 and self.front != -1:
                    self.rear = index
                else:
                    self.front = 0
                    self.rear = self.cap - 1
            print(f'queue initialised with front={self.front}, rear={self.rear}, cap={self.cap}, queue={self.queue}')


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
        # if the queue was not empty, then reset value pointed to by front
        element = self.queue[self.front]

        # remove element from queue
        self.queue[self.front] = None

        # if this was the last element, e.g. both front and rear point to the same element,
        # then reset pointers
        if self.front == self.rear:
            self.front = self.rear = -1
        # otherwise, increase front index
        else:
            self.front += 1
        return element

    def peek(self):
        return self.queue[self.front]


class CircularQueue:
    # constructor
    def __init__(self, array=None, cap=None):
        if array is None and cap is None:
            print('Please specify either array or cap.')
            return
        if cap is not None:
            self.cap = (cap - 1)
            if array is not None:
                self.cap = len(array - 1)
        self.front = -1
        self.rear = -1
        if cap is not None:
            self.queue = [None] * cap
            if array is not None:
                self.queue = array

    def is_full(self):
        # queue is full in 2 scenarios:
        # 1. if front pointer exceeds rear pointer by 1 - this happens when we've
        # populated circularly
        # 2. if front pointer is 0 and the rear pointer is at the cap -
        # this happens when we haven't dequeued or if we've circularly populated
        # to the point where we return to this configuration
        return bool((self.front == 0 and self.rear == self.cap)
                    or self.front == self.rear + 1)

    def is_empty(self):
        return Queue.is_empty(self)

    def enqueue(self, item):
        # throw overflow error if the queue is full
        if self.is_full():
            print('Queue is full.')
            return
        if self.front == -1:
            self.front = 0
        self.rear += 1
        # assign new pointer to var
        circle_rear = self.rear % (self.cap + 1)
        if self.rear >= (self.cap + 1):
            self.rear = circle_rear
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print('Queue is empty.')
            return
        # if the queue was not empty, then reset value pointed to by front
        element = self.queue[self.front]

        # remove element from queue
        self.queue[self.front] = None


        # if this was the last element, e.g. both front and rear point to the same element,
        # then reset pointers
        if self.front == self.rear:
            self.front = self.rear = -1
        # otherwise, increase front index
        # if this was not the last element, then we circularly increase the front pointer
        else:
            self.front += 1
            circle_front = self.front % (self.cap + 1)
            if self.front >= (self.cap + 1):
                self.front = circle_front
        return element

def reverse_queue(queue):
    if not queue.is_empty():
        ele = queue.dequeue()
        reverse_queue(queue)
        queue.enqueue(ele)
    return queue

def pop_specified_element_from_queue(queue, j):
    """ This function takes a queue and an integer as an input, and returns the element of the queue
    at the given index."""
    size = queue.cap
    temp = []
    for i in range(size):
        i += 1
        if i == j:
            ele = queue.dequeue()
        temp.append(queue.dequeue())
    queue = Queue(array=temp)
    return {'element': ele,
            'queue': queue}

def reverse_k_elements(queue, k):
    # we want to pop elements and increment until the increment is equal to the length of the queue,
    # subtracted by the number of elements we want to reverse

    # assign input to a temporary variable to avoid editions during for loop
    temp = Queue(cap=queue.cap)
    result = Queue(cap=queue.cap)

    size = len(queue.queue)
    for i in range(size):
        i += 1
        print(f'check if {i} = {k}')
        if i <= k:
            # assign var to popped element
            print(f'popping element {k+1-i} from {queue.queue}')
            pop = pop_specified_element_from_queue(queue, k+1-1)
            element = pop.get('element')
            after_pop_queue = pop.get('queue').queue
            print(f'after pop, element is {element} and queue is {after_pop_queue}')
            # add popped element to output variable
            result.enqueue(element)
            print(f'result queue is now {result.queue}')
            queue = Queue(array=after_pop_queue)
            print(f'input queue is now {queue.queue}\n')

        else:
            result.enqueue(queue.dequeue())
            print(f'did not equal, do normal enqueue.\n queue is now {result.queue}\n')


    print(f'for i={i}, queue is {queue.queue}')
    return temp

x=Queue(array=[1,2,3,4,5])
reverse_k_elements(x,3)
