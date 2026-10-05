class Stack:
    def __init__(self):
        self.data = []

    def push(self, aktivitas):
        self.data.append(aktivitas)

    def pop(self):
        if self.data:
            return self.data.pop()
        return None

    def peek(self):
        if self.data:
            return self.data[-1]
        return None

    def tampilkan(self):
        print(self.data)