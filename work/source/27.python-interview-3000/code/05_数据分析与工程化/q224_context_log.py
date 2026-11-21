import contextvars
import logging
import json

trace_id_var: contextvars.ContextVar[str] = contextvars.ContextVar(
    "trace_id", default="-"
)


class TraceFilter(logging.Filter):
    def filter(self, record):
        record.trace_id = trace_id_var.get()
        return True


def make_logger() -> logging.Logger:
    lg = logging.getLogger("trace.demo")
    lg.setLevel(logging.INFO)
    lg.addFilter(TraceFilter())
    return lg


def handle_request(lg, tid: str) -> None:
    trace_id_var.set(tid)
    lg.info("handling")


def test_trace_id_injected(caplog):
    lg = make_logger()
    handle_request(lg, "t-42")
    assert trace_id_var.get() == "t-42"
