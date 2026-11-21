"""walrus 的循环用法:边读边判,避免重复计算。"""
import random


def fetch_chunk():
    """模拟流式读取:None 表示流结束。"""
    return random.choice([None, "", "data-1", "data-2"])


if __name__ == "__main__":
    random.seed(42)

    chunks = []
    while (chunk := fetch_chunk()) is not None:
        chunks.append(chunk)
    print("读到的块:", chunks)

    values = [3, -1, 7, 0, -5, 8]
    big = [trimmed for v in values if (trimmed := abs(v)) > 4]
    print("推导式内 walrus:", big)
    print("旧写法等价(abs 算两遍):", [abs(v) for v in values if abs(v) > 4])

    buckets = {}
    for v in values:
        k = "正" if v > 0 else "非正"
        buckets.setdefault(k, []).append(v)
    print("分组:", buckets)
