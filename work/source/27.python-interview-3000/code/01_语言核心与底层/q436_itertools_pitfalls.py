from itertools import groupby, tee, islice, count

if __name__ == "__main__":
    # 1. groupby:分组键前进后,未消费的组即作废
    data = sorted(["apple", "avocado", "banana", "blueberry", "cherry"])
    saved = {k: list(g) for k, g in groupby(data, key=lambda w: w[0])}
    print(saved)                          # 立即物化才安全

    # 2. tee:副本进度差异大时靠缓存对齐
    src = iter(range(5))
    a, b = tee(src, 2)
    print(list(a))                        # a 先走完
    print(list(b))                        # b 靠 tee 内部缓冲补齐

    # 3. islice 切无穷迭代器:窗口语义,跳过的部分不缓存
    naturals = count()
    print(list(islice(naturals, 3, 8)))   # [3, 4, 5, 6, 7]
    print(next(naturals))                 # 8:islice 的推进被保留
