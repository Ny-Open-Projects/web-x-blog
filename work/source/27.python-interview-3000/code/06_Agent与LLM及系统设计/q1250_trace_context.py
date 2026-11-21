"""分布式追踪桩:trace 上下文注入与解析 + span 树构建 + 采样决策。"""
import itertools, random


class Span:
    _ids = itertools.count(1)

    def __init__(self, trace_id, span_id, parent_id, service, name):
        self.trace_id, self.span_id, self.parent_id = trace_id, span_id, parent_id
        self.service, self.name, self.attrs = service, name, {}

    def inject(self):
        """W3C traceparent 桩:version-traceid-spanid-flags。"""
        return f"00-{self.trace_id}-{self.span_id}-01"

    @staticmethod
    def extract(header):
        try:
            _, trace_id, parent_id, flags = header.split("-")
            return trace_id, parent_id, flags == "01"
        except ValueError:
            return None, None, False


class Tracer:
    def __init__(self, sample_rate=1.0, seed=1):
        self.spans, self.sample_rate = [], sample_rate
        random.seed(seed)

    def start(self, service, name, carrier=None):
        if carrier:
            trace_id, parent_id, sampled = Span.extract(carrier)
            sampled = sampled and random.random() < self.sample_rate or (not carrier and False)
        else:
            trace_id, parent_id = f"tr{next(Span._ids):032d}", "0" * 16
            sampled = random.random() < self.sample_rate
        span = Span(trace_id, f"sp{next(Span._ids):016x}", parent_id, service, name)
        span.attrs["sampled"] = bool(sampled)
        self.spans.append(span)
        return span

    def tree(self, trace_id):
        nodes = [s for s in self.spans if s.trace_id == trace_id]
        by_parent = {}
        for s in nodes:
            by_parent.setdefault(s.parent_id, []).append(s)
        def render(pid, depth=0):
            out = []
            for s in sorted(by_parent.get(pid, []), key=lambda x: x.span_id):
                out.append("  " * depth + f"{s.service}/{s.name}")
                out += render(s.span_id, depth + 1)
            return out
        return render("0" * 16)


if __name__ == "__main__":
    tracer = Tracer(sample_rate=1.0)
    root = tracer.start("gateway", "GET /order")
    ctx = root.inject()                            # 传播给下游
    print("traceparent:", ctx)
    child = tracer.start("order-svc", "query_order", carrier=ctx)
    ctx2 = child.inject()
    grandchild = tracer.start("payment-svc", "rpc", carrier=ctx2)

    t = root.trace_id
    lines = tracer.tree(t)
    for line in lines:
        print(" ", line)
    assert len(lines) == 3, "三服务 span 构成树"
    assert child.trace_id == root.trace_id == grandchild.trace_id, "同一 trace 串联"
    assert child.parent_id == root.span_id
    # 采样决策传递:flags=00 时不采
    tid, pid, sampled = Span.extract("00-" + "t" * 32 + "-" + "s" * 16 + "-00")
    assert sampled is False
    print("采样标志随上下文传播,全链路同采同丢")
