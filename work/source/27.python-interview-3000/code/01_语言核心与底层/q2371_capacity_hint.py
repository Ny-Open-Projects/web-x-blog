"""容量提示参数:按预期规模一次分配,省掉反复扩容。"""
import timeit


def collect_bad(stream):
    out = bytearray()
    for chunk in stream:
        out += chunk            # 不断扩容搬移
    return bytes(out)


def collect_good(stream, expected_total):
    out = bytearray(expected_total)   # 按提示一次分配
    pos = 0
    for chunk in stream:
        end = pos + len(chunk)
        if end > len(out):            # 提示不足时兜底增长
            out.extend(bytes(end - len(out)))
        out[pos:end] = chunk
        pos = end
    return bytes(out[:pos])


if __name__ == "__main__":
    stream = [b"x" * 100] * 200
    print("结果一致:", collect_bad(stream) == collect_good(stream, 20000))

    t1 = timeit.timeit(lambda: collect_bad(stream), number=2000)
    t2 = timeit.timeit(lambda: collect_good(stream, 20000), number=2000)
    print(f"无提示: {t1:.3f}s | 带容量提示: {t2:.3f}s")

    print("提示为 0 也正确:", collect_good(stream, 0) == collect_bad(stream))

    slots = [None] * 5
    slots[2] = "数据"
    print("预占位:", slots)
