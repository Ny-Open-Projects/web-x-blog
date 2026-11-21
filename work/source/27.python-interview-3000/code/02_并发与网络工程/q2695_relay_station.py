# -*- coding: utf-8 -*-
"""综合设计题: 迷你消息中继站的治理面。

五道治理设施各司其职, 任何一道失守都会变成线上事故:
- 入口双队列: 高低优先级, 加权 3:1 轮询, 低优先级延迟有上界;
- 每消费者信用: 信用守恒可对账, 慢消费者只冻住自己;
- 水位记账: 每消费者在途深度有峰值, 是容量规划的原始数据;
- 状态报告线程: 周期性输出账本, 相当于中继站的 thread dump;
- 优雅关闭: 停收 -> 排空 -> 对账, 三步收干净, 一条不丢。
"""
import threading
import time
from collections import deque

TOTAL = 300
CREDIT = 4


class Relay:
    def __init__(self):
        self.lock = threading.Lock()
        self.not_empty = threading.Condition(self.lock)
        self.credit_cv = threading.Condition(self.lock)   # 与 not_empty 共用锁
        self.hi = deque()
        self.lo = deque()
        self.ingest_done = False
        self.stopped = False
        self.pick = 0
        self.dispatch_i = 0
        self.dispatch_order = ["fast", "fast", "slow"]    # 2:1 分流
        self.dispatched = 0
        self.max_inbox = {"fast": 0, "slow": 0}
        self.consumers = {
            "fast": {"inbox": deque(), "credit": CREDIT,
                     "delivered": 0, "work": 0.001},
            "slow": {"inbox": deque(), "credit": CREDIT,
                     "delivered": 0, "work": 0.012},
        }

    # ---- 入口 ----
    def ingest(self):
        for i in range(TOTAL):
            with self.lock:
                (self.hi if i % 10 == 0 else self.lo).append(i)
                self.not_empty.notify_all()
            time.sleep(0.0005)
        with self.lock:
            self.ingest_done = True
            self.not_empty.notify_all()

    # ---- 调度: 加权轮询 + 每消费者信用 ----
    def schedule(self):
        while True:
            with self.lock:
                while not self.hi and not self.lo and not self.ingest_done:
                    self.not_empty.wait()
                if not self.hi and not self.lo and self.ingest_done:
                    return                                # 入口排空, 收工
                if self.pick % 4 == 3 and self.lo:        # 每 4 拍让 1 拍给低队列
                    q = self.lo
                elif self.hi:
                    q = self.hi
                else:
                    q = self.lo
                target = None
                for _ in range(3):                        # 轮着找有信用的人
                    name = self.dispatch_order[self.dispatch_i % 3]
                    self.dispatch_i += 1
                    if self.consumers[name]["credit"] > 0:
                        self.consumers[name]["credit"] -= 1
                        target = name
                        break
                if target is None:                        # 全员没信用: 等归还
                    self.credit_cv.wait(timeout=0.02)
                    continue
                self.consumers[target]["inbox"].append(q.popleft())
                self.dispatched += 1
                self.pick += 1
                self.max_inbox[target] = max(
                    self.max_inbox[target], len(self.consumers[target]["inbox"]))
                self.not_empty.notify_all()

    # ---- 消费者 ----
    def consume(self, name):
        box = self.consumers[name]
        while True:
            with self.lock:
                while not box["inbox"]:
                    if self.stopped:
                        return
                    self.not_empty.wait(timeout=0.05)
                if not box["inbox"]:
                    continue
                box["inbox"].popleft()
            time.sleep(box["work"])                       # 干活不占锁
            with self.lock:
                box["delivered"] += 1
                box["credit"] += 1                        # 归还信用
                self.credit_cv.notify_all()

    # ---- 状态报告 ----
    def report(self, stop_report):
        while not stop_report.is_set():
            with self.lock:
                print("  [账本] hi=%d lo=%d | fast 在途=%d 已送=%d 信用=%d"
                      " | slow 在途=%d 已送=%d 信用=%d"
                      % (len(self.hi), len(self.lo),
                         len(self.consumers["fast"]["inbox"]),
                         self.consumers["fast"]["delivered"],
                         self.consumers["fast"]["credit"],
                         len(self.consumers["slow"]["inbox"]),
                         self.consumers["slow"]["delivered"],
                         self.consumers["slow"]["credit"]))
            time.sleep(0.25)


if __name__ == "__main__":
    relay = Relay()
    stop_report = threading.Event()
    threads = [
        threading.Thread(target=relay.ingest, name="ingest", daemon=True),
        threading.Thread(target=relay.schedule, name="scheduler", daemon=True),
        threading.Thread(target=relay.consume, args=("fast",), name="c-fast", daemon=True),
        threading.Thread(target=relay.consume, args=("slow",), name="c-slow", daemon=True),
        threading.Thread(target=relay.report, args=(stop_report,), name="reporter", daemon=True),
    ]
    for t in threads:
        t.start()

    # 优雅关闭三步: 等入口收完 -> 等全部送达 -> 停机对账
    while relay.dispatched < TOTAL or any(
            len(c["inbox"]) for c in relay.consumers.values()):
        time.sleep(0.02)
    while sum(c["delivered"] for c in relay.consumers.values()) < TOTAL:
        time.sleep(0.02)
    with relay.lock:
        relay.stopped = True
        relay.not_empty.notify_all()
    stop_report.set()
    for t in threads[:4]:
        t.join(timeout=3)

    fast = relay.consumers["fast"]
    slow = relay.consumers["slow"]
    print("对账: 送达 %d/%d, 信用归还 %d/%d, 最大在途 fast=%d slow=%d"
          % (fast["delivered"] + slow["delivered"], TOTAL,
             fast["credit"] + slow["credit"], 2 * CREDIT,
             relay.max_inbox["fast"], relay.max_inbox["slow"]))
    print("要点: 信用守恒 + 送达对账, 中继站关得干不干净, 账本说了算")
