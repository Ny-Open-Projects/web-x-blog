from __future__ import annotations

import time
from typing import Optional

class Span:
    def __init__(self, name: str, parent_id: Optional[int] = None):
        self.name = name
        self.parent_id = parent_id
        self.t0 = time.perf_counter()

    def end(self):
        self.ms = round((time.perf_counter() - self.t0) * 1000, 1)

trace = []
root = Span("GET /orders")
trace.append(root)
child = Span("SELECT orders", parent_id=0)
trace.append(child)
time.sleep(0.01)
child.end()
root.end()
for s in trace:
    print(s.name, "parent:", s.parent_id, "ms:", s.ms)
