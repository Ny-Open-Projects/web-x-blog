import sys
import tracemalloc

class Plain:
    def __init__(self, x, y):
        self.x, self.y = x, y

class Slotted:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x, self.y = x, y

print("plain has dict:", Plain(1, 2).__dict__)
s = Slotted(1, 2)
print("slotted has dict:", hasattr(s, "__dict__"))          # False
try:
    s.z = 3
except AttributeError as e:
    print("blocked:", e)

tracemalloc.start()
plains = [Plain(i, i) for i in range(100_000)]
p_size = tracemalloc.get_traced_memory()[0]
del plains; tracemalloc.reset_peak()
slots_ = [Slotted(i, i) for i in range(100_000)]
s_size = tracemalloc.get_traced_memory()[0]
print("plain", round(p_size / 2**20, 1), "MB vs slotted", round(s_size / 2**20, 1), "MB")
print("per-instance delta:", sys.getsizeof(Plain(1, 2).__dict__), "bytes dict saved")
