---
title: [Q7143] 多 worker 定时任务单飞 leader 选举复盘
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7143 · 多 worker 下定时任务重复执行复盘（leader 选举）

难度：P6-P7 | 标签：gunicorn、定时任务、事故复盘

**问**：gunicorn 起 4 个 worker，每个 worker 里用 APScheduler 注册了同一个夜间对账任务，上线后每晚数据被对账 4 遍、还互相覆盖。为什么"进程里能跑的定时任务"放到多 worker 服务里就错？怎么根治？

**答**：结论：Web 服务进程的职责是"无状态响应请求"，worker 数量是运维参数，把有状态的单例任务（定时调度、后台消费）内嵌进 Web 进程，等于让任务随 worker 数量翻倍，且扩缩容/单 worker 重启都会改变任务拓扑。根治是**把调度从服务进程剥离**：独立 scheduler 进程/容器 + 分布式锁选 leader；或改成队列任务由 worker 领取（天然单飞）。临时止血用 DB advisory lock 包住任务体（Q6591）。

实战要点：
1. 判别准则：任何"应该全局只有一份在跑"的循环，不允许写在应用工厂/`app = ...` 之后；CI 里 grep `scheduler.add_job|while True` 守门。
2. leader 选举的最小实现：锁要有租约+自动续期，leader 崩溃后接管延迟=租约时长；别用"文件锁+无超时"（进程死了锁可能不释放）。
3. 接管时要处理"前 leader 跑到一半"：任务本身幂等（对账按批次键去重），否则选举切换又会双跑。

```python
"""DB advisory-lock 单飞封装 + 租约续期（标准库模拟，可运行）"""
import time
import threading


class LeaseLock:
    """带租约的分布式锁（模拟 DB advisory lock）"""

    def __init__(self, name: str, ttl: float = 30.0) -> None:
        self.name = name
        self.ttl = ttl
        self._owner: str | None = None
        self._expires = 0.0
        self._mu = threading.Lock()

    def acquire(self, holder: str) -> bool:
        with self._mu:
            now = time.monotonic()
            if self._owner is None or now >= self._expires:
                self._owner, self._expires = holder, now + self.ttl
                return True
            return False

    def renew(self, holder: str) -> bool:
        with self._mu:
            if self._owner == holder and time.monotonic() < self._expires:
                self._expires = time.monotonic() + self.ttl
                return True
            return False

    def release(self, holder: str) -> None:
        with self._mu:
            if self._owner == holder:
                self._owner = None


lock = LeaseLock("nightly-reconcile", ttl=1.0)

# worker-1 拿到 leader，worker-2 立刻拿不到
assert lock.acquire("worker-1")
assert not lock.acquire("worker-2")

# 任务体：只有 leader 跑，且跑前先续租（长任务防过期双主）
def run_job(holder: str) -> str:
    if not lock.renew(holder):
        return f"{holder}: lost leadership, abort"
    lock.release(holder)
    return f"{holder}: job done, single-flight"

print(run_job("worker-1"))
print(run_job("worker-2"))  # 已释放，worker-2 现在可接管 -> 下轮再单飞
```

**追问 1**：为什么不直接给 APScheduler 配 `max_instances=1` 就够了？
**提示**：那只管单进程内的重复实例；4 个 worker 是 4 个互不相识的调度器，进程间要去重必须外部锁或独立调度器。

**追问 2**：改成"独立 scheduler 容器"后，它自己挂了怎么办？
**提示**：scheduler 也部署多副本，内部仍用同一把租约锁选 leader——单飞靠锁，高可用靠副本数。

## 背诵要点
- 单例任务禁止内嵌 Web worker：worker 数是运维参数，任务拓扑不能跟着翻倍。
- 单飞=租约锁（advisory lock/Redis lease），高可用=多副本抢同一把锁。
- 任务体必须幂等，否则 leader 切换瞬间仍会双跑。

## 复盘追问
- 当时 4 遍对账互相覆盖，为什么数据只是"重复计算"而不是"脏数据"？
- 如果任务要改成小时级，租约与续期周期怎么重算？
