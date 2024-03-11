import main

def test_create_queue():
    x = main.Queue(cap=3)
    assert x.queue == [0, 0, 0]

def test_full_queue():
    x = main.Queue(cap=3)
    x.rear = 3
    assert main.Queue.is_full(x) is True
