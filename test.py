import pytest
import main

def test_create_queue():
    x = main.Queue(cap=3)
    assert x.queue == [0, 0, 0]
