import contextlib
from contextlib import ExitStack, contextmanager

@contextmanager
def timer(label):
    import time
    start = time.perf_counter()
    try:
        yield label
    finally:
        print(f"{label}: {time.perf_counter() - start:.4f}s")

if __name__ == "__main__":
    with timer("work"):
        sum(range(100_000))

    with ExitStack() as stack:
        stack.enter_context(timer("inner"))
        files = [stack.enter_context(open(f"/dev/null")) for _ in range(2)]
        stack.callback(print, "cleanup callback runs on exit")
    print("ExitStack done")

    with contextlib.suppress(FileNotFoundError):
        open("no_such_file_here")
    print("suppress swallows the error")
