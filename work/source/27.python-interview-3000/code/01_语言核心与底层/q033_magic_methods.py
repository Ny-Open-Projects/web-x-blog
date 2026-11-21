import functools

@functools.total_ordering
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f"Money({self.amount})"

    def __eq__(self, other):
        return isinstance(other, Money) and self.amount == other.amount

    def __lt__(self, other):
        return self.amount < other.amount

    def __add__(self, other):
        return Money(self.amount + other.amount)

    def __hash__(self):
        return hash(self.amount)

if __name__ == "__main__":
    a, b = Money(3), Money(5)
    print(a + b, a < b, a == Money(3))
    print(sorted([b, a]))
    print(len({a, b}))       # 可哈希才能进 set
