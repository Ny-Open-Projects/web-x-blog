# -*- coding: utf-8 -*-
"""threading.stack_size 与线程内存账。

- 每线程独立栈, macOS 默认走系统 pthread 栈, 可用 stack_size 调低;
- 栈太小会撞 RecursionError 甚至直接段错误, 调前必须留足最坏深度;
- 换算: 10 万线程 x 8MB 默认栈 = 800GB 虚拟内存, 上限从来不是 CPU。
"""
import threading


def work(depth, out, idx):
    def climb(n):
        if n <= 0:
            return 0
        return 1 + climb(n - 1)
    try:
        climb(depth)             # 温和深度: 各档栈都能安全承载
        out[idx] = "ok"
    except RecursionError:
        out[idx] = "recursion-error"


def main():
    old = threading.stack_size()
    print("默认 stack_size:", old, "(0 表示交给系统 pthread 默认)")

    for size in (256 * 1024, 128 * 1024, 64 * 1024, 1):
        try:
            threading.stack_size(size)
            print("set(%7d) 成功, 当前 %6d KB" %
                  (size, threading.stack_size() // 1024))
        except (ValueError, RuntimeError) as e:
            print("set(%7d) 失败: %s: %s" % (size, type(e).__name__, e))

    threading.stack_size(256 * 1024)     # 降到可用的较小值
    out = [None] * 4
    ts = [threading.Thread(target=work, args=(100, out, i))
          for i in range(4)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    threading.stack_size(old)
    print("256KB 栈跑 4 线程递归深度 100:", out)
    print("深度越大越危险: 栈不足时报 RecursionError, 更深处直接段错误")
    print("内存账: 100000 线程 x 8MB 默认 = %.0f GB (不可行)" %
          (100000 * 8 / 1024))
    print("内存账: 100000 线程 x 256KB = %.0f GB (依然巨大)" %
          (100000 * 0.25 / 1024))
    print("结论: 线程上限由栈内存与调度决定, 不是 CPU 核数")


if __name__ == "__main__":
    main()
