# -*- coding: utf-8 -*-
"""notify 的两个细节: 通知不记账, 唤醒有配额。

- notify 在无等待者时调用, 通知直接蒸发, 条件变量没有记忆;
- notify(n) 最多唤醒 n 个, 其余继续睡, 哪怕队列里还有 n 份资源;
- 所以唤醒配额要与资源数量匹配, 谓词循环 wait 是唯一安全姿势。
"""
import threading
import time


def lost_notify_demo():
    """先 notify 后 wait: 通知丢失, 消费者只能靠超时逃生。"""
    cond = threading.Condition()
    box = []

    def late_consumer():
        with cond:
            ok = cond.wait(timeout=0.3)     # 谓词不成立, 也没人再通知
            if not ok:
                box.append("timeout")
            else:
                box.append("woken")

    t = threading.Thread(target=late_consumer)
    t.start()
    time.sleep(0.1)                          # 保证消费者已进入 wait
    with cond:
        cond.notify()                        # 此时无人等待? 不, 已有人等
    t.join()
    early = box[-1]

    # 真正的丢失场景: notify 发生在 wait 之前
    cond2 = threading.Condition()
    box2 = []

    def consumer_after():
        time.sleep(0.2)                      # 故意错过通知窗口
        with cond2:
            ok = cond2.wait(timeout=0.3)
            box2.append("woken" if ok else "timeout")

    t2 = threading.Thread(target=consumer_after)
    t2.start()
    time.sleep(0.05)
    with cond2:
        cond2.notify()                       # 此刻没人等待, 通知蒸发
    t2.join()
    return early, box2[-1]


def notify_quota_demo():
    """3 个等待者只 notify(2), 第三个人哪怕醒来也抢不到锁外资源。"""
    cond = threading.Condition()
    woke = []

    def waiter(i):
        with cond:
            got = cond.wait(timeout=0.8)     # True=被通知唤醒 False=超时
            woke.append("notify" if got else "timeout")

    threads = [threading.Thread(target=waiter, args=(i,)) for i in range(3)]
    for t in threads:
        t.start()
    time.sleep(0.15)                         # 三人全部挂起
    with cond:
        cond.notify(2)                       # 配额只有 2
    for t in threads:
        t.join(timeout=2.0)
    return woke


def main():
    on_time, missed = lost_notify_demo()
    print("通知及时到达时消费者:", on_time)
    print("通知先于 wait 发出, 消费者最终:", missed)
    n = notify_quota_demo()
    print("3 个等待者 notify(2) 的结局:", n)
    assert missed == "timeout", "wait 之前的 notify 必须丢失"
    assert n.count("notify") == 2 and n.count("timeout") == 1, \
        "notify(2) 只应唤醒两人, 第三人只能超时"


if __name__ == "__main__":
    main()
