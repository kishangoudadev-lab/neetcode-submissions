class MinStack:
    lst = []
    def __init__(self):
        self.lst = []
    def push(self, val: int) -> None:
        self.lst.append(val)

    def pop(self) -> None:
        self.lst.pop()

    def top(self) -> int:
        return self.lst[-1]

    def getMin(self) -> int:
        x = sorted(self.lst)
        return x[0]
