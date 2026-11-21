
def inject_failure(kind: str, service: dict) -> str:
    if kind == "latency":
        service["p99_ms"] *= 2
        return "注入 200ms 延迟, 观察 SLO 与重试行为"
    if kind == "error":
        service["error_rate"] += 0.02
        return "注入 2% 错误, 验证熔断与降级"
    if kind == "kill":
        return "杀一个实例, 验证摘流与自愈"
    return "未知故障类型"

svc = {"p99_ms": 200, "error_rate": 0.001}
print(inject_failure("latency", svc))
print(inject_failure("error", svc))
print(inject_failure("kill", svc))
