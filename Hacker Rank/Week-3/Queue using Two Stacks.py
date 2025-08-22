class MyQueue:
    def __init__(self):
        self.inp = []
        self.out = []

    def enqueue(self, x):
        self.inp.append(x)

    def dequeue(self):
        self._transfer_if_needed()
        if self.out:
            self.out.pop()

    def peek(self):
        self._transfer_if_needed()
        if self.out:
            return self.out[-1]

    def _transfer_if_needed(self):
        if not self.out:
            while self.inp:
                self.out.append(self.inp.pop())


def queries():
    q = int(input().strip())
    queue = MyQueue()
    for _ in range(q):
        query = input().strip().split()
        if query[0] == "1":
            queue.enqueue(int(query[1]))
        elif query[0] == "2":
            queue.dequeue()
        elif query[0] == "3":
            print(queue.peek())

if __name__ == "__main__":
    queries()
