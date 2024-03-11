import pytest

import main

# Create fixture for empty queue
@pytest.fixture
def empty_queue():
    return main.Queue(cap=3)


def non_empty_queue():
    x = main.Queue(cap=3)
    x.enqueue(1)
    return x


def test_create_queue(empty_queue):
    assert empty_queue.queue == [0, 0, 0]
    assert empty_queue.front == -1
    assert empty_queue.rear == -1
    assert empty_queue.cap == 3


def test_full_queue_is_full(empty_queue):
    empty_queue.rear = 3
    assert main.Queue.is_full(empty_queue) is True


def test_empty_queue_is_empty(empty_queue):
    assert main.Queue.is_empty(empty_queue) is True


def test_empty_queue_is_not_full(empty_queue):
    assert main.Queue.is_full(empty_queue) is False

def test_enqueue_initialised_queue(empty_queue):
    main.Queue.enqueue(empty_queue, 1)
    assert empty_queue.front == 0
    assert empty_queue.rear == 0
    assert empty_queue.queue == [1, 0, 0]
