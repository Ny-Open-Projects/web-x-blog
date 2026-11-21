"""通用重试装饰器:指数退避 + 抖动 + 异常白名单。"""
import functools
import logging
import random
import time

log = logging.getLogger(__name__)


def retry(exceptions=(Exception,), attempts=3, base_delay=0.1, max_delay=2.0):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == attempts:
                        raise
                    delay = min(base_delay * 2 ** (attempt - 1), max_delay)
                    delay += random.uniform(0, delay * 0.3)  # jitter 防惊群
                    log.warning("%s 第 %s 次失败 %s,%.2fs 后重试",
                                func.__name__, attempt, e, delay)
                    time.sleep(delay)
        return wrapper
    return deco


class TransientError(Exception):
    pass


_calls = {"n": 0}


@retry(exceptions=(TransientError,), attempts=4, base_delay=0.05)
def flaky_api():
    """前两次失败,第三次成功,模拟抖动的下游。"""
    _calls["n"] += 1
    if _calls["n"] < 3:
        raise TransientError("upstream 503")
    return {"ok": True, "call": _calls["n"]}


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print(flaky_api())
