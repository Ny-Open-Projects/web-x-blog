"""调试输出走 stderr:不污染 stdout 的数据管道。"""
import sys


def debug(*args):
    """统一调试出口:stderr 加立即刷新。"""
    print("[debug]", *args, file=sys.stderr, flush=True)


def process(numbers):
    """正常输出只有结果,stdout 保持纯数据。"""
    return [n * 2 for n in numbers]


if __name__ == "__main__":
    data = [1, 2, 3]
    debug("输入:", data)
    result = process(data)
    debug("输出:", result)
    print(*result)                    # 只有结果进 stdout

    captured = []

    class ListWriter:
        def write(self, s):
            captured.append(s)

        def flush(self):
            pass

    real = sys.stdout
    sys.stdout = ListWriter()
    try:
        print("数据行")
        debug("这一行去了 stderr,不混进 stdout")
    finally:
        sys.stdout = real
    print("stdout 只捕到:", captured)
