# -*- coding: utf-8 -*-
"""毒丸与超时双保险: 正常关门靠毒丸, 异常情况靠空闲超时兜底。

- 毒丸是显式关门协议, 干净但脆弱: 生产者先死, 消费者就永远等不到它;
- get(timeout) 的空闲超时是最后的保险丝, 连续 N 个窗口无事发生就撤退;
- 双保险的顺序很重要: 先看毒丸, 再数空闲, 谁先到谁触发。
"""
import queue
import threading
import time

PILL = object()


def consumer(q, log, idle_limit=3, window=0.1):
    idle_windows = 0
    while True:
        try:
            item = q.get(timeout=window)
        except queue.Empty:
            idle_windows += 1
            if idle_windows >= idle_limit:
                log.append("超时保险丝: 连续 %d 个窗口无事, 撤退" % idle_limit)
                return
            continue
        idle_windows = 0
        if item is PILL:
            log.append("毒丸: 正常关门")
            return
        log.append("处理 %s" % item)


def main():
    # 场景一: 生产者健康, 毒丸生效
    q1 = queue.Queue()
    log1 = []
    t1 = threading.Thread(target=consumer, args=(q1, log1), daemon=True)
    t1.start()
    for i in range(3):
        q1.put("任务%d" % i)
        time.sleep(0.02)
    q1.put(PILL)
    t1.join(timeout=2)
    print("健康路径:")
    for line in log1:
        print("  ", line)
    assert any("毒丸" in x for x in log1), "毒丸应触发正常关门"

    # 场景二: 生产者中途暴毙, 永远不会有毒丸, 超时兜底
    q2 = queue.Queue()
    log2 = []
    t2 = threading.Thread(target=consumer, args=(q2, log2), daemon=True)
    t2.start()
    q2.put("任务0")
    time.sleep(0.05)
    print("事故路径: 生产者不再投递, 也不投毒丸")
    t2.join(timeout=2)
    assert not t2.is_alive(), "超时保险丝必须让消费者退出"
    for line in log2:
        print("  ", line)
    tail = log2[-1]
    assert "超时保险丝" in tail, "最后应是超时兜底触发"

    # 对照: 没有超时的裸 get 消费者将永远悬在队列上
    print("对照: 若只有毒丸没有超时, 场景二的消费者会永久悬停")


if __name__ == "__main__":
    main()
