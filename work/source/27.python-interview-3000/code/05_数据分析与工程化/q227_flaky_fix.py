import random


def flaky_network_stub(fail_rate=0.0):
    # 修法:把网络依赖替换为确定性 stub,而不是祈祷它别抖
    def call():
        if random.random() < fail_rate:
            raise ConnectionError
        return {"status": "ok"}
    return call


def poll_until(check, max_attempts=10):
    # 修法二:轮询条件代替 sleep 猜时间
    for _ in range(max_attempts):
        if check():
            return True
    return False


def test_deterministic():
    stub = flaky_network_stub(fail_rate=0.0)
    assert stub()["status"] == "ok"

def test_no_sleep_guessing():
    assert poll_until(lambda: True) is True
    assert poll_until(lambda: False, max_attempts=3) is False
