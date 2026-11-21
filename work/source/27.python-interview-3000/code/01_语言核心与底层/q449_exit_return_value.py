import contextlib

class Intercept:
    def __init__(self, swallow):
        self.swallow = swallow

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        name = exc_type.__name__ if exc_type else None
        print(f"exit sees: {name}")
        return self.swallow               # True:异常到此为止

class Replacer:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        raise RuntimeError("replaced inside exit")

if __name__ == "__main__":
    with Intercept(swallow=True):
        raise ValueError("swallowed")
    print("continues normally")

    try:
        with Intercept(swallow=False):
            raise ValueError("propagates")
    except ValueError as e:
        print("caught outside:", e)

    try:
        with Replacer():
            raise ValueError("original")
    except RuntimeError as e:
        print("new:", e, "| context:", repr(e.__context__))

    with contextlib.suppress(KeyError):
        {"a": 1}["b"]
    print("suppress done")
