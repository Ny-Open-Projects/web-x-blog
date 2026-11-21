import time


def wait_until(check, timeout: float = 5.0, interval: float = 0.5) -> bool:
    # 应用侧就绪等待:比 depends_on 更可靠的服务依赖处理
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if check():
            return True
        time.sleep(interval)
    return False


def test_wait_until_ready():
    attempts = {"n": 0}

    def ready():
        attempts["n"] += 1
        return attempts["n"] >= 3

    assert wait_until(ready, timeout=2) is True
