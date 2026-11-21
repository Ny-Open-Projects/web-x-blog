# -*- coding: utf-8 -*-
"""隔离舱满载的快速失败与降级: 降级值让调用方永远拿到可用答案。

- 满载或执行超时都不许向调用方抛裸异常, 统一转成降级值;
- 降级延迟必须远小于正常调用, 快速失败才有意义;
- 记录降级原因分类, 是容量问题还是健康问题要分得清。
"""
import concurrent.futures
import threading
import time


class BulkheadFull(Exception):
    pass


class Bulkhead:
    def __init__(self, name, permits):
        self.name = name
        self._sem = threading.BoundedSemaphore(permits)
        self._pool = concurrent.futures.ThreadPoolExecutor(
            max_workers=permits, thread_name_prefix=name)

    def call(self, fn, wait=0.05, run_timeout=2.0):
        if not self._sem.acquire(timeout=wait):
            raise BulkheadFull("隔离舱 %s 已满" % self.name)
        try:
            return self._pool.submit(fn).result(timeout=run_timeout)
        finally:
            self._sem.release()


def resilient_call(bulkhead, fn, fallback_value, wait=0.05):
    t0 = time.monotonic()
    try:
        return bulkhead.call(fn, wait=wait), "primary", time.monotonic() - t0
    except BulkheadFull as e:
        return fallback_value, "fallback:" + type(e).__name__, \
            time.monotonic() - t0
    except concurrent.futures.TimeoutError:
        return fallback_value, "fallback:TimeoutError", time.monotonic() - t0


def main():
    bh = Bulkhead("recommend-慢服务", 2)
    start = threading.Event()
    outcomes = []

    def slow_recommend():
        time.sleep(0.3)
        return "真实推荐"

    def user(i):
        start.wait()
        value, kind, cost = resilient_call(bh, slow_recommend,
                                           fallback_value="热门榜单")
        outcomes.append((i, value, kind, cost))

    ts = [threading.Thread(target=user, args=(i,)) for i in range(10)]
    for t in ts:
        t.start()
    time.sleep(0.02)
    start.set()
    for t in ts:
        t.join(timeout=3.0)

    primary = [x for x in outcomes if x[2] == "primary"]
    fallback = [x for x in outcomes if x[2].startswith("fallback")]
    print("主路径成功 %d 个, 降级 %d 个" % (len(primary), len(fallback)))
    print("降级原因分布:", {k: sum(1 for x in fallback if x[2] == k)
                           for k in set(x[2] for x in fallback)})
    print("降级耗时上限: %.4fs, 主路径耗时: %.2fs"
          % (max(x[3] for x in fallback), primary[0][3]))
    assert len(primary) == 2 and len(fallback) == 8, "舱位 2, 其余全走降级"
    assert all(v == "热门榜单" for _, v, _, _ in fallback)
    # 断言采用确定性设计: 绝对墙钟受机器负载影响, 改为以同一次运行的主路径实测耗时为锚——
    # 降级路径最多等 wait=0.05s 就放弃, 必须显著快于 0.3s 的真实慢调用 (低于其一半)
    assert max(x[3] for x in fallback) < primary[0][3] / 2, "降级必须快速失败"
    assert primary[0][3] >= 0.3, "主路径是真实慢调用"
    assert all(v == "真实推荐" for _, v, _, _ in primary)
    print("结论: 降级是兜底的答案不是抛错, 容量问题与健康问题分类记账")


if __name__ == "__main__":
    main()
