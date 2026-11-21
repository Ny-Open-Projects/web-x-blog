"""装饰器 + 上下文管理器 + 生成器的组合实战:流式审计计时器。"""
import time
from contextlib import contextmanager
from functools import wraps


def audit_stream():
    """生成器:逐条接收审计记录并即时打印,体现惰性消费。"""
    while True:
        record = yield
        status = "OK " if record["ok"] else "ERR"
        tail = record["error"] or ""
        print(f"[{status}] {record['section']:<6} {record['elapsed']:.4f}s {tail}")


@contextmanager
def audit(section, sink):
    """上下文管理器:负责计时与异常标注,退出时把记录交给 sink。"""
    start = time.perf_counter()
    record = {"section": section, "ok": True, "error": None, "elapsed": 0.0}
    try:
        yield record
    except Exception as exc:
        record["ok"] = False
        record["error"] = type(exc).__name__
        raise
    finally:
        record["elapsed"] = time.perf_counter() - start
        sink.send(record)


def timed(sink):
    """装饰器工厂:把函数调用包进 audit 上下文。"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with audit(func.__name__, sink):
                return func(*args, **kwargs)
        return wrapper
    return decorator


stream = audit_stream()
next(stream)                      # 预激生成器


@timed(stream)
def work(n):
    time.sleep(0.01)
    return n * 2


@timed(stream)
def boom():
    raise ValueError("boom")


if __name__ == "__main__":
    print("返回值:", work(21))
    try:
        boom()
    except ValueError as e:
        print("捕获业务异常:", e)
    stream.close()
