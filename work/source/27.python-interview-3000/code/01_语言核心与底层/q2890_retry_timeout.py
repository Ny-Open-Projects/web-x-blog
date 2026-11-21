"""重试与超时的统一原语:deadline 感知的 run_with_retry。"""
import random
import time


class AttemptFailed(Exception):
    pass


def run_with_retry(func, args=(), kwargs=None, *, attempts=5,
                   base_delay=0.01, deadline_s=1.0, retry_on=(AttemptFailed,)):
    """统一原语:整体 deadline 优先于重试次数,指数退避加抖动。"""
    kwargs = kwargs or {}
    started = time.monotonic()
    last_exc = None
    for i in range(1, attempts + 1):
        if time.monotonic() - started >= deadline_s:
            raise TimeoutError(f"deadline 已到,共尝试 {i - 1} 次")
        try:
            return func(*args, **kwargs)
        except retry_on as exc:
            last_exc = exc
            if i == attempts:
                break
            delay = base_delay * 2 ** (i - 1) + random.uniform(0, base_delay)
            if time.monotonic() - started + delay > deadline_s:
                raise TimeoutError(f"退避将越过 deadline,放弃于第 {i} 次后") from exc
            time.sleep(delay)
    raise AttemptFailed(f"{attempts} 次尝试全部失败,最后一次:{last_exc!r}")


class Flaky:
    """模拟前几次必失败的下游调用。"""

    def __init__(self, fail_times=2):
        self.fail_times = fail_times
        self.calls = 0

    def __call__(self):
        self.calls += 1
        if self.calls <= self.fail_times:
            raise AttemptFailed(f"第 {self.calls} 次抖动")
        return "ok"


if __name__ == "__main__":
    random.seed(7)
    flaky = Flaky(fail_times=2)
    print("重试成功:", run_with_retry(flaky), "实际调用", flaky.calls, "次")

    always = Flaky(fail_times=99)
    try:
        run_with_retry(always, attempts=3, base_delay=0.005)
    except AttemptFailed as e:
        print("次数耗尽:", e)

    started = time.monotonic()
    try:
        run_with_retry(Flaky(fail_times=99), attempts=50, base_delay=0.05, deadline_s=0.12)
    except TimeoutError as e:
        print("deadline 截停:", e, f"耗时 {time.monotonic() - started:.2f}s")
