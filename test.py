import pytest

import main

# Create fixture for empty queue
@pytest.fixture
def init_queue():
    return main.Queue(cap=3)

def test_create_queue(init_queue):
    assert init_queue.queue == [0, 0, 0]
    assert init_queue.front == -1
    assert init_queue.rear == -1
    assert init_queue.cap == 3


def test_full_queue(init_queue):
    init_queue.rear = 3
    assert main.Queue.is_full(init_queue) is True


def test_enqueue_initialised_queue(init_queue):
    main.Queue.enqueue(init_queue, 1)
    assert init_queue.front == 0
    assert init_queue.rear == 0
    assert init_queue.queue == [1, 0, 0]
