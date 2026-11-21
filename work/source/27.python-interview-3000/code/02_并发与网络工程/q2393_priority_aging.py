# -*- coding: utf-8 -*-
"""优先级队列的老化: 等待时间变硬通货, 低优先级也要有出头日。

- 同步老化是个陷阱: 所有条目一起涨分, 相对差距不变, 低优照样垫底;
- 正解是只给低于天花板的任务发等待补贴, 涨到天花板为止, 先等先赢;
- 出堆时线性扫描重算有效优先级, O(n) 的代价买一个不会饿死的世界。
"""
import threading
import time


class AgingPriorityQueue:
    def __init__(self, aging_rate=0.0, boost_ceiling=None):
        self._items = []                 # [基础优先级, 序号, 负载, 入队时刻]
        self._seq = 0
        self._cond = threading.Condition()
        self._rate = aging_rate          # 每等 1 秒补多少有效优先级
        self._ceiling = boost_ceiling    # 补贴封顶: 只救低于天花板的任务

    def put(self, pri, payload):
        with self._cond:
            self._items.append((pri, self._seq, payload, time.monotonic()))
            self._seq += 1
            self._cond.notify()

    def _eff(self, pri, enq, now):
        if self._ceiling is None or pri >= self._ceiling:
            return pri                   # 高于天花板的不补贴, 相对差距才会缩小
        return min(pri + self._rate * (now - enq), self._ceiling)

    def take(self):
        with self._cond:
            while not self._items:
                self._cond.wait(timeout=0.2)
            now = time.monotonic()
            best_i, best_key = 0, None
            for i, (pri, seq, payload, enq) in enumerate(self._items):
                key = (self._eff(pri, enq, now), -seq)   # 先等先赢
                if best_key is None or key > best_key:
                    best_i, best_key = i, key
            return self._items.pop(best_i)[2]


EVENTS = [(5, "高优-1"), (0, "低优-受苦者"),
          (5, "高优-2"), (5, "高优-3"), (5, "高优-4")]


def replay(rate, ceiling):
    """全部入队后停顿 0.5 秒再消费: 补贴在真实等待时间里确定性累积, 出场顺序可复现。"""
    q = AgingPriorityQueue(aging_rate=rate, boost_ceiling=ceiling)
    for pri, name in EVENTS:
        q.put(pri, name)
    time.sleep(0.5)                  # 低优补贴 20/s * 0.5s 涨到天花板 5, 与高优同分
    out = []
    while len(out) < len(EVENTS):
        out.append(q.take())
    return out


def main():
    out_plain = replay(0.0, None)
    out_aging = replay(20.0, 5)
    print("静态优先级出队:", out_plain)
    print("补贴 20/s 出队:", out_aging)
    assert out_plain[-1] == "低优-受苦者", "静态堆里低优必须垫底"
    idx = out_aging.index("低优-受苦者")
    assert idx < 4, "补贴到顶后低优必须出头"
    assert any(x.startswith("高优") for x in out_aging[idx + 1:]), \
        "低优出头之后还有高优在后, 才证明是补贴提权而非运气"


if __name__ == "__main__":
    main()
