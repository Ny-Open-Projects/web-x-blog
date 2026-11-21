import threading

REGISTRY = {}

class Counter:
    def __init__(self, name):
        self.name = name
        self.value = 0
        self.lock = threading.Lock()
        REGISTRY[name] = self

    def inc(self, n=1):
        with self.lock:
            self.value += n

class Histogram:
    def __init__(self, name, buckets):
        self.name = name
        self.buckets = buckets
        self.counts = [0] * len(buckets)   # 累积桶
        self.total = 0
        self.count = 0
        self.lock = threading.Lock()
        REGISTRY[name] = self

    def observe(self, v):
        with self.lock:
            for i, b in enumerate(self.buckets):
                if v <= b:
                    self.counts[i] += 1
            self.total += v
            self.count += 1

if __name__ == "__main__":
    req = Counter("http_requests_total")
    lat = Histogram("http_request_seconds", [0.01, 0.05, 0.1, 0.5])
    req.inc()
    req.inc()
    for v in (0.004, 0.03, 0.2):
        lat.observe(v)
    print(req.name, req.value)
    print(lat.name, dict(zip(lat.buckets, lat.counts)), "count", lat.count)
