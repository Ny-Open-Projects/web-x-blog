---
title: [Q797] beat 定时任务与分布式锁
date: 2026-11-17
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q797 · beat 定时任务与分布式锁

> 难度:★★★☆ | 标签:Celery, 定时任务

**问**:beat 多实例部署会怎样?定时任务的防重怎么做才稳?

**答**:beat 靠本地调度表投递,多实例会**重复投递**,所以 beat 全局只跑一个(k8s 单副本/主备选主)。防重双保险:任务内部再加**分布式锁**(Redis SETNX 带 TTL 或数据库行锁),锁命中直接退出,防 beat 重叠调度、人工误触发和消息重复。锁要有 TTL 防死锁、执行时长要续期或控制在 TTL 内;定时窗口错峰(避开整点)也能降低碰撞概率。

```python
# file: code/03_Web后端开发/q797_beat_lock.py
import time

lock_store: dict = {}

def try_lock(name: str, ttl: float) -> bool:
    now = time.time()
    holder = lock_store.get(name)
    if holder and holder > now:
        return False
    lock_store[name] = now + ttl
    return True

def nightly_job() -> str:
    if not try_lock("nightly-report", ttl=3600):
        return "已被其他节点执行"
    return "执行报表生成"

print(nightly_job())
print(nightly_job())
```

**追问**:
- 锁的 TTL 比任务执行时间短了怎么办?——用带续期的看门狗(执行中定期延长 TTL),或把 TTL 设为任务上限并接受偶发双跑配合幂等。
- 任务延迟执行怎么补偿?——记录计划执行时间,任务开头检查当前时间与计划的偏差,超窗任务跳过或告警。
