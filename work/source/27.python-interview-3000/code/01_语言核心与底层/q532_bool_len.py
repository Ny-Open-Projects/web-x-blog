class Queue:
    def __init__(self, items):
        self._items = list(items)

    def __len__(self):
        print("  __len__ called")
        return len(self._items)

    def push(self, x):
        self._items.append(x)

    def pop(self):
        return self._items.pop(0)

class AlwaysTrue:
    def __len__(self):
        return 0

    def __bool__(self):
        return True                       # __bool__ 优先于 __len__

if __name__ == "__main__":
    q = Queue([])
    print("empty:", bool(q))              # 回退 __len__ → 0 → False
    q.push("job")
    print("nonempty:", bool(q))
    if q:
        print("if q: truthy branch")

    print("bool wins over len:", bool(AlwaysTrue()))
    print("default is truthy:", bool(object()))
