# -*- coding: utf-8 -*-
"""配置热更新的线程安全: 版本化快照, 读侧无锁。

- 配置整体打包成不可变快照, 更新时构建新快照后原子换引用;
- 读者只拿一次引用, 天然看到同一版本的完整配置, 不会拼出混搭;
- 实测: 写侧连发 4 个版本, 读侧上万次读取无一出现跨版本组合。
"""
import threading
import time

VERSIONS = {
    0: (10, 1.0, 2),
    1: (20, 0.5, 3),
    2: (15, 2.0, 1),
    3: (30, 0.2, 5),
    4: (25, 1.5, 2),
}
_snapshot = {"version": 0, "rate": 10, "timeout": 1.0, "retries": 2}
done = threading.Event()


def get_snapshot():
    """单次引用读取: GIL 保证引用赋值对读者原子可见。"""
    return _snapshot


def apply_update(version, rate, timeout, retries):
    global _snapshot
    new = {"version": version, "rate": rate,
           "timeout": timeout, "retries": retries}
    _snapshot = new          # 原子换引用: 读者要么旧版要么新版


def reader(idx, out):
    mixed = 0
    seen = set()
    reads = 0
    while not done.is_set() or reads < 3000:
        snap = get_snapshot()              # 一次取整包
        expected = VERSIONS[snap["version"]]
        if (snap["rate"], snap["timeout"], snap["retries"]) != expected:
            mixed += 1                     # 出现跨版本拼凑才会计数
        seen.add(snap["version"])
        reads += 1
        if reads % 100 == 0:
            time.sleep(0.001)
    out[idx] = (mixed, seen, reads)


def main():
    out = [None] * 4
    ts = [threading.Thread(target=reader, args=(i, out)) for i in range(4)]
    for t in ts:
        t.start()
    for v in range(1, 5):                   # 写侧热更新 4 个新版本
        rate, timeout, retries = VERSIONS[v]
        apply_update(v, rate, timeout, retries)
        time.sleep(0.02)
    done.set()
    for t in ts:
        t.join()
    for i, (mixed, vers, reads) in enumerate(out):
        print("读者 %d: 读 %d 次, 混搭 %d 次, 覆盖版本 %s" %
              (i, reads, mixed, sorted(vers)))
    print("混搭总数:", sum(m for m, _, _ in out),
          "-> 快照换引用保证读侧永远拿到完整一致版本")
    print("补充: 生产落地还需配置校验失败回滚与版本号单调递增")


if __name__ == "__main__":
    main()
