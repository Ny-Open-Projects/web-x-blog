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
