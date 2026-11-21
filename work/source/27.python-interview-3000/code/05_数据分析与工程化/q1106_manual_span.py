import itertools
import time

_ids = itertools.count(1)

class Span:
    def __init__(self, tracer, name, parent=None):
        self.id = next(_ids)
        self.name = name
        self.parent = parent
        self.tracer = tracer
        self.attrs = {}
        self.children = []
        self.dur_ms = None

    def __enter__(self):
        self.t0 = time.perf_counter()
        if self.parent:
            self.parent.children.append(self)
        return self

    def __exit__(self, *exc):
        self.dur_ms = (time.perf_counter() - self.t0) * 1000
        self.tracer.finished.append(self)

    def set_attr(self, k, v):
        self.attrs[k] = v

class Tracer:
    def __init__(self):
        self.finished = []

    def span(self, name, parent=None):
        return Span(self, name, parent)

    def render(self, span, depth=0):
        print("  " * depth + f"span {span.id} {span.name} {span.dur_ms:.1f}ms {span.attrs}")
        for c in span.children:
            self.render(c, depth + 1)

if __name__ == "__main__":
    tr = Tracer()
    with tr.span("http request") as root:
        root.set_attr("method", "GET")
        with tr.span("db query", parent=root) as s:
            s.set_attr("table", "orders")
        with tr.span("render", parent=root):
            pass
    tr.render(root)
    # 真实 OTel:with tracer.start_as_current_span("db_query") as span: span.set_attribute(...)
