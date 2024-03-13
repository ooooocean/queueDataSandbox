import pytest
import main


# verify that creating a queue works correctly

class TestQueue:
    def test_queue(self):
        empty_queue = main.Queue(cap=3)
        print(empty_queue)
        assert empty_queue.queue == [None, None, None]
        assert empty_queue.front == -1
        assert empty_queue.rear == -1
        assert empty_queue.cap == 2

    # once it works, use this as a fixture
    @pytest.fixture
    def empty_queue(self):
        return main.Queue(cap=3)

    def test_enqueue_one_item_to_empty_queue(self, empty_queue):
        # verify that
        main.Queue.enqueue(empty_queue, 1)
        assert empty_queue.front == 0
        assert empty_queue.rear == 0
        assert empty_queue.queue == [1, None, None]
        main.Queue.enqueue(empty_queue, 1)
        assert empty_queue.front == 0
        assert empty_queue.rear == 1
        assert empty_queue.queue == [1, 1, None]
        main.Queue.enqueue(empty_queue, 1)
        assert empty_queue.front == 0
        assert empty_queue.rear == 2
        assert empty_queue.queue == [1, 1, 1]

    @pytest.fixture()
    def non_empty_queue(self):
        z = main.Queue(cap=3)
        z.front = 0
        z.rear = 0
        z.queue[0] = 1
        return z

    @pytest.fixture()
    def full_queue(self):
        y = main.Queue(cap=3)
        y.front = 0
        y.rear = 2
        y.queue = [1] * 3
        return y

    def test_enqueue_to_full_queue(self, full_queue):
        main.Queue.enqueue(full_queue, 1)
        assert full_queue.front == 0
        assert full_queue.rear == 2
        assert full_queue.queue == [1, 1, 1]

    def test_dequeue_empty_queue(self, empty_queue):
        # dequeue an empty queue
        main.Queue.dequeue(empty_queue)
        assert empty_queue.front == -1
        assert empty_queue.rear == -1
        assert empty_queue.queue == [None, None, None]

    def test_dequeue_non_empty_queue(self):
        # dequeue a queue which has only one element in the front
        a = main.Queue(cap=3)
        a.front = 0
        a.rear = 0
        a.queue = [1, None, None]
        assert main.Queue.dequeue(a) == 1
        assert a.front == -1
        assert a.rear == -1
        assert a.queue == [None, None, None]

        # dequeue a queue which has only one element in the middle
        b = main.Queue(cap=3)
        b.front = 1
        b.rear = 1
        b.queue = [None, 1, None]
        assert main.Queue.dequeue(b) == 1
        assert b.front == -1
        assert b.rear == -1
        assert b.queue == [None, None, None]

        # dequeue a queue which has only one element in the end
        c = main.Queue(cap=3)
        c.front = 2
        c.rear = 2
        c.queue = [None, None, 1]
        assert main.Queue.dequeue(c) == 1
        assert c.front == -1
        assert c.rear == -1
        assert c.queue == [None, None, None]

    def test_dequeue_full_queue(self, full_queue):
        assert main.Queue.dequeue(full_queue) == 1
        assert full_queue.front == 1
        assert full_queue.rear == 2
        assert full_queue.queue == [None, 1, 1]

        assert main.Queue.dequeue(full_queue) == 1
        assert full_queue.front == 2
        assert full_queue.rear == 2
        assert full_queue.queue == [None, None, 1]

        assert main.Queue.dequeue(full_queue) == 1
        assert full_queue.front == -1
        assert full_queue.rear == -1
        assert full_queue.queue == [None, None, None]

    def test_is_empty(self, empty_queue, non_empty_queue, full_queue):
        assert empty_queue.is_empty() is True
        assert non_empty_queue.is_empty() is False
        assert full_queue.is_empty() is False

    def test_is_full(self, empty_queue, non_empty_queue, full_queue):
        assert empty_queue.is_full() is False
        assert non_empty_queue.is_full() is False
        assert full_queue.is_full() is True

    def test_peek(self, empty_queue, full_queue):
        assert empty_queue.peek() == None
        assert full_queue.peek() == 1

class TestCircularQueue:

    def test_circular_queue_creation(self):
        x = main.CircularQueue(cap=3)
        assert x.queue == [None, None, None]
        assert x.front == -1
        assert x.rear == -1
        assert x.cap == 2

    @pytest.fixture
    def empty_queue(self):
        return main.CircularQueue(cap=3)

    def test_circular_queue_is_full(self):
        x = main.CircularQueue(cap=3)
        x.queue = [1, 1, 1]
        x.front = 0
        x.rear = 2
        assert x.is_full() is True

        x.front = 1
        x.rear = 0
        assert x.is_full() is True

        x.front = 2
        x.rear = 1
        assert x.is_full() is True

        x.front = 2
        x.rear = 0
        assert x.is_full() is False

        x.front = x.rear = 1
        assert x.is_full() is False

    def test_circular_queue_enqueue_to_full_queue(self):
        x = main.CircularQueue(cap = 3)
        x.queue = [1, 1, 1]
        x.front = 0
        x.rear = 2
        main.CircularQueue.enqueue(x, 1)
        assert x.front == 0
        assert x.rear == 2
        assert x.queue == [1, 1, 1]

        x.front = 1
        x.rear = 0
        main.CircularQueue.enqueue(x, 1)
        assert x.front == 1
        assert x.rear == 0
        assert x.queue == [1, 1, 1]

        x.front = 2
        x.rear = 1
        main.CircularQueue.enqueue(x, 1)
        assert x.front == 2
        assert x.rear == 1
        assert x.queue == [1, 1, 1]

def test_circular_queue_enqueue_to_non_empty_queue():
    x = main.CircularQueue(cap=3)
    x.queue = [None, 1, 1]
    x.front = 1
    x.rear = 2
    main.CircularQueue.enqueue(x, 1)
    assert x.front == 1
    assert x.rear == 0
    assert x.queue == [1, 1, 1]

    x.queue = [1, None, 1]
    x.front = 2
    x.rear = 3
    main.CircularQueue.enqueue(x, 1)
    assert x.front == 2
    assert x.rear == 1
    assert x.queue == [1, 1, 1]

def test_circular_queue_dequeue_to_non_empty_queue():
    x = main.CircularQueue(cap=3)
    x.queue = [None, 1, 1]
    x.front = 1
    x.rear = 2
    main.CircularQueue.dequeue(x)
    assert x.front == 2
    assert x.rear == 2
    assert x.queue == [None, None, 1]

    x.queue = [1, None, 1]
    x.front = 2
    x.rear = 0
    main.CircularQueue.dequeue(x)
    assert x.front == 0
    assert x.rear == 0
    assert x.queue == [1, None, None]


def test_reverse_queue():
    x = main.Queue(array=[4, 3, 1, 10, 2, 6])
    main.reverse_queue(x)
    assert x.queue == [6, 2, 10, 1, 3, 4]

    x = main.Queue(array=[1, 2, 3, 4])
    main.reverse_queue(x)
    assert x.queue == [4, 3, 2, 1]

def test_non_repeating_helper():
    assert main.first_non_repeating_helper('aabc') == 'b'
    assert main.first_non_repeating_helper('zz') == '#'
    assert main.first_non_repeating_helper('aabbccddeef') == 'f'