from Deque_Generator import get_deque

class Queue:

  def __init__(self):
    self._dq = get_deque()

  def __str__(self):
    return str(self._dq)

  def __len__(self):
    return len(self._dq)

  def enqueue(self, val):
    return self._dq.push_back(val)

  def dequeue(self):
    return self._dq.pop_front()

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
