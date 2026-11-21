"""请求日志采样:错误全采、噪声丢弃、确定性头部采样(纯标准库)。"""
import hashlib


def should_log(trace_id, status, base_rate=0.1):
    if status >= 500:
        return "keep", "error-full-sample"
    if status in (404, 429):
        return "drop", "noise-filter"
    h = int(hashlib.sha256(trace_id.encode()).hexdigest(), 16) % 10_000
    if h < base_rate * 10_000:
        return "keep", "head-sample"
    return "drop", "sampled-out"


kept = sum(1 for i in range(1000) if should_log(f"trace-{i}", 200)[0] == "keep")
print("200 请求按 10% 保留:", kept, "/1000")
print("5xx 全采:", should_log("t-x", 500))
print("404 丢弃:", should_log("t-y", 404))
print("确定性:", should_log("trace-42", 200) == should_log("trace-42", 200))
