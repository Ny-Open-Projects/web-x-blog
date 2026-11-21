
BUCKETS = [0.005, 0.01, 0.05, 0.1, 0.5, 1.0]
LATENCIES = [0.003, 0.008, 0.02, 0.12, 0.6]

def hist_counts(values):
    counts = [0] * (len(BUCKETS) + 1)   # 最后一位是 +Inf
    for v in values:
        placed = False
        for i, b in enumerate(BUCKETS):
            if v <= b:
                counts[i] += 1
                placed = True
                break
        if not placed:
            counts[-1] += 1
    return counts

def render(name, counts):
    lines = [f"# HELP {name} request duration", f"# TYPE {name} histogram"]
    cum = 0
    for b, c in zip(BUCKETS, counts[:-1]):
        cum += c
        lines.append(f'{name}_bucket{{le="{b}"}} {cum}')
    lines.append(f'{name}_bucket{{le="+Inf"}} {sum(counts)}')
    return "\n".join(lines)

if __name__ == "__main__":
    print(render("http_request_duration_seconds", hist_counts(LATENCIES)))
    print("# gauge 示例: queue_depth 42")
    print("# counter 示例: http_requests_total 1024")
