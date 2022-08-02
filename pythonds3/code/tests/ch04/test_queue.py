from src.ch04.queue import Queue


def test_queue_creation():
    Queue()


def test_enqueue_dequeue():
    q = Queue()
    q.enqueue('abc')
    q.enqueue('def')

    assert q.dequeue() == 'abc'
    assert q.dequeue() == 'def'
    assert q.size() == 0


def test_size():
    q = Queue()
    assert q.size() == 0

    q.enqueue('abc')
    assert q.size() == 1

    q.dequeue()
    assert q.size() == 0


def test_is_empty():
    q = Queue()
    assert q.is_empty()

    q.enqueue('abc')
    assert not q.is_empty()
