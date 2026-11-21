from dataclasses import dataclass, field
import time


@dataclass
class Span:
    name: str
    trace_id: str
    start: float = field(default_factory=time.monotonic)
    children: list = field(default_factory=list)

    def duration_ms(self) -> float:
        return (time.monotonic() - self.start) * 1000


def build_trace():
    root = Span("http GET /orders", trace_id="t1")
    db = Span("db query", trace_id="t1")
    root.children.append(db)
    return root


def test_trace_structure():
    trace = build_trace()
    assert trace.name.startswith("http")
    assert trace.children[0].name == "db query"
    assert trace.trace_id == "t1"
