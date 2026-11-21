# -*- coding: utf-8 -*-
"""优先级继承与天花板协议: 用协作调度器模拟解法。

- 优先级继承: 持锁者临时继承最高等待者的优先级, 尽快干完放锁;
- 优先级天花板: 临界区一开始就运行在全体可能等待者的最高优先级上;
- 用单线程协作调度器把规则跑出来: 每个时钟节拍选最高有效优先级的就绪任务。
"""

LOW, MID, HIGH = 1, 2, 3


class Resource:
    def __init__(self, inherit):
        self.owner = None
        self.waiters = []
        self.inherit = inherit

    def acquire(self, task):
        if self.owner is None:
            self.owner = task
            return True
        self.waiters.append(task)
        task.ready = False                     # 没拿到锁就挂起
        if self.inherit and task.base_prio > self.owner.eff_prio:
            self.owner.eff_prio = task.base_prio   # 继承: 抬高持锁者
        return False

    def release(self):
        self.owner = None
        for w in self.waiters:
            w.eff_prio = w.base_prio
            w.ready = True
        self.waiters = []


class Task:
    def __init__(self, name, prio, body, start_tick=0):
        self.name = name
        self.base_prio = prio
        self.eff_prio = prio
        self.body = body
        self.start_tick = start_tick
        self.entered = start_tick == 0
        self.ready = start_tick == 0
        self.done = False
        self.log = []


def low_body(res):
    res.acquire(CURRENT["t"])
    yield "got-lock"
    for i in range(4):
        yield "work-%d" % i
    res.release()
    yield "released"


def high_body(res):
    while not res.acquire(CURRENT["t"]):
        yield "wait"
    yield "got-lock"
    res.release()
    yield "released"


def mid_body():
    for i in range(3):
        yield "pure-work-%d" % i


def simulate(inherit, ticks=16):
    global CURRENT
    CURRENT = {"t": None}
    res = Resource(inherit)
    tasks = [
        Task("low", LOW, low_body(res)),
        Task("mid", MID, mid_body(), start_tick=1),
        Task("high", HIGH, high_body(res), start_tick=2),
    ]
    trace = []
    for tick in range(ticks):
        for t in tasks:
            if not t.entered and tick >= t.start_tick:
                t.entered = True            # 到点入场, 只此一次
                t.ready = True
        ready = [t for t in tasks if t.ready and not t.done]
        if not ready:
            break
        cur = max(ready, key=lambda t: t.eff_prio)
        CURRENT["t"] = cur
        try:
            ev = next(cur.body)
            cur.log.append((tick, cur.eff_prio, ev))
            trace.append("%d:%s[%d]%s" % (tick, cur.name, cur.eff_prio, ev))
        except StopIteration:
            cur.done = True
    high_got = next((tick for tick, _, ev in tasks[2].log if ev == "got-lock"),
                    None)
    return trace, high_got


def main():
    trace0, got0 = simulate(inherit=False)
    print("无继承 trace:", " | ".join(trace0))
    print("无继承: high 第 %s 拍才拿到锁, mid 在其等待期间完成 3 拍纯工作" % got0)

    trace1, got1 = simulate(inherit=True)
    print("有继承 trace:", " | ".join(trace1))
    print("有继承: low 的有效优先级被抬到 %d, high 第 %s 拍拿到锁" %
          (HIGH, got1))
    print("结论: 继承让持锁者优先清空临界区, 反转窗口被压缩")


if __name__ == "__main__":
    main()
