---
title: [Q1303] 优雅降级开关:线程可见的 feature toggle
date: 2026-11-17
categories: [Python并发与网络]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1303 · 优雅降级开关:线程可见的 feature toggle

> 难度:★★☆☆ | 标签:降级开关, feature toggle, 原子快照

**问**:线上出事了,怎么在不重启进程的前提下把某个功能"一键关掉"?

**答**:降级开关的本质是一个"线程间可见的布尔量",工程要点有三个。第一,可见性:Python 里 dict 的单项修改是原子的,但"检查开关再执行"不是——所以开关要用整体替换的不可变快照,请求开始时取一次快照,整条请求路径用同一份,避免中途开关翻转导致行为分裂。第二,快照要小:开关面板最多几十个键,整份复制毫无压力,千万别做成"每个请求都去查配置中心"。第三,自动降级:手动开关之外,通常再挂一个错误率触发器,连续失败超阈值自动翻开关,恢复后自动(或人工确认)翻回来。下面的演示里主线程翻转开关,工作线程持续服务并在每个请求开头取一次快照,统计两个阶段各自的命中次数。

```python
# file: code/02_并发与网络工程/q1303_degrade_switch.py
import threading
import time


class DegradeSwitch:
    """开关面板: 整体替换不可变快照, 请求粒度取一次、全程一致。"""

    def __init__(self, features: dict) -> None:
        self._lock = threading.Lock()
        self._snapshot = dict(features)   # {功能名: 是否可用}

    def snapshot(self) -> dict:
        with self._lock:
            return dict(self._snapshot)   # 请求开始时取一次

    def set_all(self, features: dict) -> None:
        with self._lock:
            self._snapshot.update(features)


def serve_request(snap: dict, feature: str, stats: dict) -> None:
    if snap.get(feature, True):
        stats["normal"] += 1              # 正常路径
    else:
        stats["degraded"] += 1            # 兜底路径: 返回缓存/默认值


def main() -> None:
    switch = DegradeSwitch({"recommend": True, "search": True})
    stats = {"normal": 0, "degraded": 0}
    stats_lock = threading.Lock()
    stop = threading.Event()

    def worker() -> None:
        while not stop.is_set():          # 持续服务, 覆盖翻转前后的所有阶段
            snap = switch.snapshot()      # 每个请求取一次快照
            with stats_lock:
                serve_request(snap, "recommend", stats)

    threads = [threading.Thread(target=worker) for _ in range(4)]
    for t in threads:
        t.start()

    time.sleep(0.3)
    print("运维翻转开关: recommend -> 关闭")
    switch.set_all({"recommend": False})
    time.sleep(0.3)
    print("恢复: recommend -> 开启")
    switch.set_all({"recommend": True})
    time.sleep(0.3)
    stop.set()

    for t in threads:
        t.join()
    print(f"正常服务 {stats['normal']} 次, 降级兜底 {stats['degraded']} 次")
    assert stats["degraded"] > 0 and stats["normal"] > 0, "两个阶段都应出现"


if __name__ == "__main__":
    main()
```

**追问**:1) 为什么请求开始取快照、而不是每步都查开关?——中途翻转会让一次请求前半段走主路径、后半段走兜底,状态不一致;请求粒度一致性是降级的底线。2) 快照模式的并发原理是什么?——开关面板做成不可变对象,翻转是「整体替换引用」,CPython 下引用赋值原子,读线程要么拿到旧快照要么新快照,都是自洽的;这与配置热更新(Q707)是同一模式。3) 自动降级(错误率触发)的防抖怎么做?——连续 N 次失败才翻开关(单次抖动不动);翻回去要么人工确认要么「半开探测」(Q1336),自动恢复配自动触发容易在故障边界来回振荡,把下游彻底打死。4) 生产陷阱?——开关检查与执行分离的窗口(检查后依赖才挂);快照里放了可变 dict 被业务改坏;降级开关只翻了一半(依赖 A 关了依赖 B 没关);恢复后没人翻回来,系统长期活在降级模式没人知道。

---
