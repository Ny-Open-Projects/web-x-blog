import functools

def my_contextmanager(func):
    """复刻 contextlib.contextmanager 的核心语义"""
    @functools.wraps(func)
    def helper(*args, **kwargs):
        return _GeneratorCM(func(*args, **kwargs))
    return helper

class _GeneratorCM:
    def __init__(self, gen):
        self.gen = gen

    def __enter__(self):
        return next(self.gen)                 # 执行到 yield,取值

    def __exit__(self, exc_type, exc, tb):
        if exc_type is None:
            try:
                next(self.gen)                # 正常:推进到函数结束
            except StopIteration:
                return False
            raise RuntimeError("generator did not stop")
        try:
            self.gen.throw(exc_type, exc, tb) # 异常:在 yield 处注入
        except StopIteration:
            return True                       # 生成器吞掉了异常 → 抑制
        except BaseException as new_exc:
            if new_exc is exc:
                return False                  # 原样重新抛出 → 继续传播
            raise new_exc from exc            # 改抛了别的异常 → 带上下文抛出

@my_contextmanager
def managed(label):
    print(f"enter {label}")
    try:
        yield label.upper()
    finally:
        print(f"exit {label}")

@my_contextmanager
def swallow_errors(label):
    print(f"enter {label}")
    try:
        yield
    except ValueError:
        print(f"{label} swallowed ValueError")
    finally:
        print(f"exit {label}")

if __name__ == "__main__":
    with managed("hello") as v:
        print("inside:", v)
    with swallow_errors("s"):
        raise ValueError("boom")
    print("survived swallow")
    try:
        with managed("m"):
            raise KeyError("pass-through")
    except KeyError as e:
        print("propagated:", e)
