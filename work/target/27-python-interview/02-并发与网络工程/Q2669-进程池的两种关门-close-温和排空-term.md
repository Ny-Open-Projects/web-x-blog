---
title: [Q2669] 进程池的两种关门:close 温和排空,terminate 立即清场
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2669 · 进程池的两种关门:close 温和排空,terminate 立即清场

> 难度:★★★ | 标签:进程池, close, terminate

**问**:进程池收尾时 close 和 terminate 的区别是什么?terminate 之后没跑的任务结果还能拿到吗?

**答**:close 是温和关门:不再收新任务,已收下的全部跑完,实测 6 个任务结果一张不少;terminate 是立即清场:worker 马上被杀,没跑的任务永远不会有结果,实测完成 2 个、4 个永远拿不到——对后者调 get() 会无限阻塞,必须带 timeout 并按 TimeoutError 处理。

- 正常收尾用 close + join,异常收尾(超时、崩溃、停机信号)才用 terminate;

- terminate 之后不要无超时地 get,那是一个新的挂死;

- 判断"哪些任务没跑"要靠业务侧登记,池不提供回执;

- concurrent.futures 的 shutdown(cancel_futures=True) 是同一主题的现代写法。

```python
# file: code/02_并发与网络工程/q2669_pool_close_terminate.py
# -*- coding: utf-8 -*-
"""进程池的两种关门: close 温和排空, terminate 立即清场。

- close: 不再收新任务, 已收下的全部跑完, 结果一张不少;
- terminate: 立即杀 worker, 没跑的任务永远不会有结果;
- 对没跑的任务调 get() 会无限等待, 必须带 timeout 兜底。
"""
import multiprocessing as mp
import time


def slow_job(i):
    time.sleep(0.15)
    return i


if __name__ == "__main__":
    # 方式一: close + join, 温和排空
    p = mp.Pool(2)
    rs = [p.apply_async(slow_job, (i,)) for i in range(6)]
    p.close()                            # 关门: 谢绝新客, 存量做完
    p.join()
    print("close 语义: 完成 %d/6, 结果 %s" % (len(rs), [r.get() for r in rs]))

    # 方式二: terminate, 立即清场
    p2 = mp.Pool(2)
    rs2 = [p2.apply_async(slow_job, (i,)) for i in range(6)]
    time.sleep(0.35)                     # 让第一批任务先做完
    p2.terminate()                       # 清场: worker 立即被杀
    p2.join()
    done, lost = 0, 0
    for r in rs2:
        try:
            r.get(timeout=0.3)
            done += 1
        except mp.TimeoutError:
            lost += 1                    # 没跑的任务: get 永远等不到
    print("terminate 语义: 完成 %d 个, 永远拿不到结果 %d 个" % (done, lost))
```

**追问**:1) terminate 时正在跑的任务会怎样?——worker 被杀,任务结果既不成功也不失败,直接蒸发,上层要靠超时或幂等兜底。2) close 之后还能 submit 吗?——不能,会抛 ValueError,这正是"关门"的语义。3) 底层机制:terminate 杀掉什么、结果为什么蒸发?——terminate 对每个 worker 发 SIGTERM 不等完成,任务与 worker 一起死,结果管道随之关闭,父进程侧的 AsyncResult 永远等不到数据,get() 无限阻塞;close 只是拒绝新任务,存量继续由存活 worker 跑完。4) 生产陷阱?——terminate 后对未完成任务无 timeout 的 get,制造新的挂死;把 terminate 当常规收尾手段,却没有幂等与重发机制;concurrent.futures 侧忘记 shutdown(cancel_futures=True),排队任务继续占资源。

---
