import pytest

import main

def test_create_queue():
    x = main.Queue(cap=3)
    assert x.queue == [0, 0, 0]
    assert x.front == -1
    assert x.rear == -1
    assert x.cap == 3


def test_full_queue():
    x = main.Queue(cap=3)
    x.rear = 3
    assert main.Queue.is_full(x) is True


# Create fixture for empty queue
@pytest.fixture
def init_queue():
    return main.Queue(cap=3)


def test_enqueue_initialised_queue(init_queue):
    main.Queue.enqueue(init_queue, 1)
    assert init_queue.front == 0
    assert init_queue.rear == 0
    assert init_queue.queue == [1, 0, 0]

