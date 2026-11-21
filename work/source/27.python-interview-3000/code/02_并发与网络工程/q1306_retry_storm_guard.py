import threading


class RetryBudget:
    """全局重试预算: 重试总量 <= 总请求量 * ratio。"""

    def __init__(self, ratio: float) -> None:
        self._ratio = ratio
        self._lock = threading.Lock()
        self._requests = 0
        self._retries = 0

    def note_request(self) -> None:
        with self._lock:
            self._requests += 1

    def allow_retry(self) -> bool:
        with self._lock:
            if self._retries < self._ratio * self._requests:
                self._retries += 1
                return True
            return False


def call_with_retries(dep, budget: RetryBudget, max_attempts: int) -> int:
    """返回本次请求对依赖发起的实际调用次数, 失败抛最后一个异常。"""
    budget.note_request()
    attempts = 1
    while True:
        try:
            dep.hit()
            return attempts
        except ConnectionError:
            if attempts < max_attempts and budget.allow_retry():
                attempts += 1      # 每一次重试都先扣预算
                continue
            raise


class DeadDependency:
    def __init__(self) -> None:
        self.hits = 0
        self._lock = threading.Lock()

    def hit(self) -> None:
        with self._lock:
            self.hits += 1
        raise ConnectionError("down")


def main() -> None:
    requests, max_attempts = 50, 3

    bare = DeadDependency()
    for _ in range(requests):
        try:
            call_with_retries(bare, RetryBudget(ratio=10.0), max_attempts)  # 等于不设限
        except ConnectionError:
            pass
    print(f"裸重试: {requests} 个请求打出 {bare.hits} 次依赖调用")

    budgeted = DeadDependency()
    budget = RetryBudget(ratio=0.2)
    for _ in range(requests):
        try:
            call_with_retries(budgeted, budget, max_attempts)
        except ConnectionError:
            pass
    print(f"预算 20%: {requests} 个请求只打出 {budgeted.hits} 次依赖调用")
    assert budgeted.hits <= requests * (1 + 0.2) + max_attempts
    assert bare.hits == requests * max_attempts
    print("重试风暴被预算压住")


if __name__ == "__main__":
    main()
