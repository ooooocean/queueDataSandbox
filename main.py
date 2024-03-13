from collections import deque

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
            self.front = 0
            self.cap = (len(array))
            self.rear = self.cap - 1

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

def first_non_repeating(string):
    # convert input string to queue
    stream = deque(string)

    # initialise comparison variable
    comparator = deque('')

    # assign length of input string
    length = len(stream)
    print(length)
    # generate substring for comparison
    for i in range(length):
        i += 1
        comparator.append(stream.popleft())
        while comparator:
            character = comparator.popleft()

def first_non_repeating_helper(string):
    """ Returns if a string has any repeating characters"""
    string = deque(string)

    # initialise var to store matched characters
    matched = []

    while string:
        print(f'input is {string} with length {len(string)}')
        character = string.popleft()
        print(f'popped {character}. input is now {string} with {len(string)}')
        length = len(string)

        if character in matched:
            print(f'character was found in {matched}, terminating substring check for {character}\n')
            if length == 0:
                character = '#'
                return character
            continue
        if length == 0:
            return character
        print(f'check if {character} is in matched list: {matched}')
        print(f'comparing {character} to {string}')
        print(f'initiate for loop for {range(length)}')

        for i in range(length):
            i += 1
            print(f'loop now compares {character} to {string[0]}')
            if character == string[0]:
                # if we match a repeating character, add it to a list of matched characters
                matched.append(string[0])
                print(f'{character} is first instance of repeat, added to matched list: {matched}\n')
                break
            # otherwise, we have not matched anything and we can return the character that did not have any repeats
            print(f'{character} is non-repeating\n')
            return character



print(first_non_repeating_helper('zz'))

