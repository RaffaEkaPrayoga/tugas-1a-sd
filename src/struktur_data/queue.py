from collections import deque


class Queue:
    def __init__(self):
        self.data = deque()

    def enqueue(self, mahasiswa):
        self.data.append(mahasiswa)

    def dequeue(self):
        if self.data:
            return self.data.popleft()
        return None

    def tampilkan(self):
        print(list(self.data))