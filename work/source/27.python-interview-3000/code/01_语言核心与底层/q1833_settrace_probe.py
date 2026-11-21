"""sys.settrace 极简行探针:执行轨迹与热点行统计。"""
import sys
from collections import Counter

HITS = Counter()


def probe(frame, event, arg):
    if event == "call":
        return probe                     # 该帧继续跟踪 line 事件
    if event == "line":
        code = frame.f_code
        if code.co_filename == __file__:
            HITS[(code.co_name, frame.f_lineno)] += 1
        return probe
    return None                          # 返回 None 表示不再跟踪该帧


def bubblesort(xs):
    for i in range(len(xs) - 1):
        for j in range(len(xs) - 1 - i):
            if xs[j] > xs[j + 1]:
                xs[j], xs[j + 1] = xs[j + 1], xs[j]
    return xs


def run_probe(func, *args):
    sys.settrace(probe)
    try:
        return func(*args)
    finally:
        sys.settrace(None)


def report(top=5):
    for (name, line), n in HITS.most_common(top):
        print("  {:>4} 次  {} 第 {} 行".format(n, name, line))


if __name__ == "__main__":
    result = run_probe(bubblesort, [5, 2, 8, 1])
    print("排序结果:", result)
    print("行级热点 Top5:")
    report()
