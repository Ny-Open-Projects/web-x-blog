# -*- coding: utf-8 -*-
"""批量任务的部分失败回传: 把每个失败连同输入一起带回来。

- 批量任务里部分失败是常态, 不能一个失败拖垮整批;
- future.exception() 只取异常不重新抛出, 批照常收完;
- 回传 (输入, 异常) 对, 上层才能精准重试失败的子集。
"""
from concurrent.futures import ProcessPoolExecutor, as_completed


def risky_parse(i):
    """i 是 3 的倍数就当作坏数据抛异常。"""
    if i % 3 == 0:
        raise ValueError("bad payload %d" % i)
    return i * 10


if __name__ == "__main__":
    inputs = list(range(9))
    oks, fails = [], []
    with ProcessPoolExecutor(max_workers=4) as ex:
        futs = {ex.submit(risky_parse, i): i for i in inputs}
        for f in as_completed(futs):
            i = futs[f]
            exc = f.exception()          # 取异常而不重新抛出
            if exc is None:
                oks.append((i, f.result()))
            else:
                fails.append((i, type(exc).__name__, str(exc)))

    print("成功 %d 个: %s" % (len(oks), sorted(oks)))
    print("失败 %d 个: %s" % (len(fails), sorted(fails)))
    print("失败输入集合可单独重试:", sorted(i for i, _, _ in fails))
