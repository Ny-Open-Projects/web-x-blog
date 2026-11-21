---
title: [Q2382] notify 的配额与丢失通知
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2382 · notify 的配额与丢失通知

> 难度:★★★ | 标签:Condition, notify, 丢失唤醒

**问**:notify 在没有等待者时调用会怎样?notify(2) 对三个等待者意味着什么?

**答**:Condition 是纯内存原语,没有记忆:notify 发出时没有人在等,通知就地蒸发,后来的 wait 只能等下一次 notify,这就是丢失通知 lost wakeup。

- 实测先 notify 后 wait,消费者只能靠超时逃生,谓词没变、通知没了;

- notify(n) 是配额制:最多放行 n 个,实测 3 个等待者 notify(2),两人被唤醒、第三人超时;

- 配额应与新增资源数量一致,放 n 件资源就 notify(n);

- 唯一的安全姿势是谓词循环:wait 返回后重查条件,不成立继续 wait,任何唤醒语义的坑都被它兜住。

```python
# file: code/02_并发与网络工程/q2382_notify_n_lost.py
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
```

**追问**:1) wait 被虚假唤醒 spurious wakeup 打断怎么办?——wait 放在 while 谓词循环里正是为此,虚假唤醒重查谓词后继续睡。2) Condition 换成 Event 能避开丢失通知吗?——Event 有状态位能记住“发生过”,但它只有一档广播,做不了按配额的精准唤醒。3) 「条件变量没有记忆」的工程含义?——通知是瞬时事件,不是状态:notify 时无等待者就蒸发;正确性只能建立在「谓词+重查」上,不能建立在「我 notify 过了」上——Event(有状态位)与 Condition(无记忆)的语义分界就在这。4) notify(n) 配额的匹配规则?——放 n 件资源 notify(n);一次放多件(批量 put)notify(len(items));配额过多=空唤醒,过少=有人饿着——「配额=新增可用量」是精确唤醒的公式,广播则是偷懒但昂贵的兜底。5) 生产陷阱?——先 notify 后改状态(通知与谓词时序倒置);依赖「notify 必达」(蒸发);Event 当队列用(只有一档广播);谓词循环里改共享状态没持锁;把 spurious wakeup 当 bug 修(它是特性,while 兜住即可)。

---
