import pytest
import main

def test_queue():
    empty_queue = main.Queue(cap=3)
    assert empty_queue.queue == [0, 0, 0]
    assert empty_queue.front == -1
    assert empty_queue.rear == -1
    assert empty_queue.cap == 3

@pytest.fixture
def empty_queue():
    return main.Queue(cap=3)

def test_enqueue(empty_queue):
    main.Queue.enqueue(empty_queue, 1)
    assert empty_queue.front == 0
    assert empty_queue.rear == 0
    assert empty_queue.queue == [1, 0, 0]

@pytest.fixture()
def non_empty_queue():
    z = main.Queue(cap=3)
    z.front = 0
    z.rear = 0
    z.queue[0] = 1
    return z

@pytest.fixture()
def full_queue():
    y = main.Queue(cap=3)
    y.front = 3
    y.rear = 3
    y.queue = [1] * 3
    return y

def test_is_empty(empty_queue, non_empty_queue, full_queue):
    assert empty_queue.is_empty() is True
    assert non_empty_queue.is_empty() is False
    assert full_queue.is_empty() is False


def test_is_full(empty_queue, non_empty_queue, full_queue):
    assert empty_queue.is_full() is False
    assert non_empty_queue.is_full() is False
    assert full_queue.is_full() is True


