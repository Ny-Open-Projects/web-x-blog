from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Span:
    trace_id: str
    span_id: str
    parent_span_id: Optional[str]
    name: str


def parse_traceparent(header: str) -> tuple[str, str]:
    # W3C Trace Context: 00-<32位traceid>-<16位spanid>-01
    parts = header.split("-")
    return parts[1], parts[2]


def child_span(header: str, name: str) -> Span:
    trace_id, parent = parse_traceparent(header)
    return Span(trace_id, "b" * 16, parent, name)


def test_trace_propagation():
    span = child_span("00-" + "a" * 32 + "-" + "b" * 16 + "-01", "downstream")
    assert span.trace_id == "a" * 32
    assert span.parent_span_id == "b" * 16
    assert span.name == "downstream"
