
def make_traceparent(trace_id: str, span_id: str, sampled: bool = True) -> str:
    flags = "01" if sampled else "00"
    return f"00-{trace_id}-{span_id}-{flags}"

def parse_traceparent(header: str) -> dict:
    _, trace_id, span_id, flags = header.split("-")
    return {"trace_id": trace_id, "span_id": span_id, "sampled": flags == "01"}

tp = make_traceparent("4bf92f3577b34da6a3ce929d0e0e4736", "00f067aa0ba902b7")
print(tp)
print(parse_traceparent(tp))
