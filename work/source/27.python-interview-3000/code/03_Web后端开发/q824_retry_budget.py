import random

def retry_call(attempts: list, max_retry: int = 3, budget_ms: float = 100) -> str:
    spent = 0.0
    for i in range(max_retry + 1):
        cost = random.uniform(10, 80)
        spent += cost
        attempts.append(f"try{i}:{cost:.0f}ms")
        if cost < 50:
            return "ok"
        if spent > budget_ms:
            attempts.append("预算耗尽 停止重试")
            break
    return "failed"

res: list = []
print(retry_call(res), res)
