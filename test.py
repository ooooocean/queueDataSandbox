import pytest
import main


# verify that creating a queue works correctly

class TestQueue:
    def test_queue(self):
        empty_queue = main.Queue(cap=3)
        assert empty_queue.queue == [0, 0, 0]
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
        assert empty_queue.queue == [1, 0, 0]
        main.Queue.enqueue(empty_queue, 1)
        assert empty_queue.front == 0
        assert empty_queue.rear == 1
        assert empty_queue.queue == [1, 1, 0]
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
        assert empty_queue.queue == [0, 0, 0]

    def test_dequeue_non_empty_queue(self):
        # dequeue a queue which has only one element in the front
        a = main.Queue(cap=3)
        a.front = 0
        a.rear = 0
        a.queue = [1, 0, 0]
        assert main.Queue.dequeue(a) == 1
        assert a.front == -1
        assert a.rear == -1
        assert a.queue == [0, 0, 0]

        # dequeue a queue which has only one element in the middle
        b = main.Queue(cap=3)
        b.front = 1
        b.rear = 1
        b.queue = [0, 1, 0]
        assert main.Queue.dequeue(b) == 1
        assert b.front == -1
        assert b.rear == -1
        assert b.queue == [0, 0, 0]

        # dequeue a queue which has only one element in the end
        c = main.Queue(cap=3)
        c.front = 2
        c.rear = 2
        c.queue = [0, 0, 1]
        assert main.Queue.dequeue(c) == 1
        assert c.front == -1
        assert c.rear == -1
        assert c.queue == [0, 0, 0]

    def test_dequeue_full_queue(self, full_queue):
        assert main.Queue.dequeue(full_queue) == 1
        assert full_queue.front == 1
        assert full_queue.rear == 2
        assert full_queue.queue == [0, 1, 1]

        assert main.Queue.dequeue(full_queue) == 1
        assert full_queue.front == 2
        assert full_queue.rear == 2
        assert full_queue.queue == [0, 0, 1]

        assert main.Queue.dequeue(full_queue) == 1
        assert full_queue.front == -1
        assert full_queue.rear == -1
        assert full_queue.queue == [0, 0, 0]

    def test_is_empty(self, empty_queue, non_empty_queue, full_queue):
        assert empty_queue.is_empty() is True
        assert non_empty_queue.is_empty() is False
        assert full_queue.is_empty() is False

    def test_is_full(self, empty_queue, non_empty_queue, full_queue):
        assert empty_queue.is_full() is False
        assert non_empty_queue.is_full() is False
        assert full_queue.is_full() is True

    def test_peek(self, empty_queue, full_queue):
        assert empty_queue.peek() == 0
        assert full_queue.peek() == 1

class TestCircularQueue:

    def test_circular_queue_creation(self):
        x = main.CircularQueue(cap=3)
        assert x.queue == [0, 0, 0]
        assert x.front == -1
        assert x.rear == -1
        assert x.cap == 2

    @pytest.fixture
    def empty_queue(self):
        return main.CircularQueue(cap=3)

    def test_circular_queue_is_full(self, x):
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
