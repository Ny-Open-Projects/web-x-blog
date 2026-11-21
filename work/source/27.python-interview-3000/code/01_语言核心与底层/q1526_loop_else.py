import time


def poll_until_ready(check, timeout=0.3, interval=0.05):
    """轮询直到 check 返回真;超时返回 None。else 承接超时分支。"""
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if check():
            return time.monotonic()   # 成功路径:直接 return,不走 else
        time.sleep(interval)
    else:
        return None                   # 循环自然耗尽 = 超时失败


def first_negative(seq):
    for x in seq:
        if x < 0:
            return x
    else:
        return None                   # 没找到:for-else 省掉 found 标志


def flip_after_two_calls():
    flip_after_two_calls.n += 1
    return flip_after_two_calls.n > 2


flip_after_two_calls.n = 0


if __name__ == "__main__":
    ok = poll_until_ready(flip_after_two_calls, timeout=1.0)
    fail = poll_until_ready(lambda: False, timeout=0.15)
    print("poll success:", ok is not None)
    print("poll timeout :", fail is None)
    print("first_negative([3, 1, -7]):", first_negative([3, 1, -7]))
    print("first_negative([3, 1]):   ", first_negative([3, 1]))
    # 空序列也算自然耗尽,else 照走——测试最容易漏的分支
    print("empty loop else:", first_negative([]))
