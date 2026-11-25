---
title: [Q7114] Celery beat 重复实例导致任务双跑事故复盘
date: 2026-11-21
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7114 · Celery beat 双实例导致定时任务双跑事故复盘

难度：P6 ｜ 标签：事故复盘 / Celery beat / 单飞

**问**：某天报表数据翻倍，排查发现夜间批任务每个都执行了两次：运维扩容时把 beat 也按 worker 副本数扩了，两个 beat 实例同时调度。beat 的单实例约束为什么这么容易破？事故后的多层次防线怎么设计？

**答**：
- **结论**：机理：beat 是**调度器**（把到期的任务发进 broker），不是执行器——它没有任何跨实例协调机制，两个 beat 就是两个独立调度器，各自把同一个 `crontab` 条目投递两次；worker 收到两条消息就跑两遍。K8s Deployment/多机部署天然鼓励"多副本"，beat 的单飞约束在部署清单里没有显式表达，扩容脚本一把梭就破坏了。根因层次：① 部署层——beat 应该是单副本 Deployment（replicas: 1）或独立 StatefulSet，且要防"滚动更新期间新旧两个 beat 并存"（maxSurge>0 时更新窗口双跑）；② 应用层——任务必须幂等（唯一键去重），调度类任务用分布式锁/数据库 advisory lock 单飞（Q6591 同源思路），幂等是最后防线不是唯一防线；③ 观测层——"同一任务短窗口内执行两次"做告警规则（trace/log 按 task_id+参数聚合），报表翻倍这种业务侧指标异常是滞后信号。
- **取舍**：单飞实现选型：① 数据库唯一键/`INSERT ... ON CONFLICT DO NOTHING` 抢占——最可靠但要为每个任务建登记；② Redis 锁（SET NX + TTL > 任务最大时长）——简单，但 TTL 与任务时长不匹配会漏（Q6543 时钟/TTL 教训）；③ K8s 原生方案——beat 用 `strategy: Recreate` 单副本 + `podAntiAffinity`，或干脆把调度收拢到外部调度器（Airflow/K8s CronJob），让 Celery 只做执行器——**架构上消灭 beat** 是更彻底的方向，代价是调度视图分散。报表/账务类任务必须"幂等 + 单飞"双保险，监控类任务可以只幂等。
- **实战**：落地：① 部署清单评审加检查项：beat/CronJob 类组件 replicas 与策略显式声明；② 任务入口统一包装 `once_lock(task_key, ttl)` 装饰器，锁失败直接放弃并记一条"skipped-duplicate"日志（不重试——重试又制造重复）；③ 批任务表带 `batch_date` 唯一键，双跑时第二条被 DB 拦截；④ 灰度验证：预发故意跑双 beat，确认防线逐层生效。

```python
# beat 双实例防线模拟：DB 唯一键幂等 + 锁单飞 双保险
# 基线：Python 3.9+ 标准库；真实场景 Celery beat + Redis 锁/PG advisory lock
import time
from dataclasses import dataclass, field


@dataclass
class BatchRegistry:
    """批任务登记表：(task, batch_date) 唯一键。"""
    seen: set[tuple[str, str]] = field(default_factory=set)

    def try_acquire(self, task: str, batch_date: str) -> bool:
        key = (task, batch_date)
        if key in self.seen:
            return False
        self.seen.add(key)
        return True


@dataclass
class TtlLock:
    owner: str | None = None
    expires: float = 0.0

    def acquire(self, owner: str, ttl_s: float, now: float) -> bool:
        if now < self.expires and self.owner != owner:
            return False
        self.owner, self.expires = owner, now + ttl_s
        return True


def run_task(registry: BatchRegistry, lock: TtlLock, task: str, date: str,
             caller: str, now: float) -> str:
    """双防线：先锁后幂等键；锁挡不住时幂等兜底。"""
    if not lock.acquire(caller, ttl_s=600, now=now):
        return "skipped-duplicate"
    if not registry.try_acquire(task, date):
        return "blocked-by-registry"
    return "executed"


def main() -> None:
    reg = BatchRegistry()
    lock = TtlLock()

    # 两个 beat 在同一时刻各投一次：第二条被锁挡
    r1 = run_task(reg, lock, "nightly_report", "2026-11-21", "beat-a", now=1000)
    r2 = run_task(reg, lock, "nightly_report", "2026-11-21", "beat-b", now=1001)
    assert r1 == "executed" and r2 == "skipped-duplicate"

    # 锁 TTL 过期后的迟到投递：锁失效，但幂等键兜底
    r3 = run_task(reg, lock, "nightly_report", "2026-11-21", "beat-b", now=2000)
    assert r3 == "blocked-by-registry"
    print("双防线生效: 锁挡并发, 唯一键挡 TTL 过期后的迟到重复")

    # 不同 batch_date 正常执行：防线不误伤（锁 TTL 已过期）
    assert run_task(reg, lock, "nightly_report", "2026-11-22", "beat-a", now=3000) == "executed"
    print("OK: beat 必须单副本部署; 幂等是最后防线不是唯一防线")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么"skipped-duplicate"不能走重试？
→ 一句话提示：这条消息本身就是重复投递，重试等于再制造一次竞争；正确行为是记录并丢弃，让登记表成为唯一事实——重试语义只该给"执行失败"而不是"判定为重复"。

**追问 2**：把调度从 beat 迁到外部调度器（K8s CronJob/Airflow）要重新设计什么？
→ 一句话提示：Celery beat 的 schedule 是代码里的静态配置，外部调度器把"什么时候调"变成平台配置——要重新设计调度变更的发布流程、失败告警归属（调度侧 vs 执行侧）与补数入口（Q7068 参数化补数同源）。

## 背诵要点
- beat 是无协调的独立调度器：多副本=任务必然双跑，部署清单必须显式单副本（含滚动更新窗口的 maxSurge 陷阱），或架构上消灭 beat（调度收拢到外部）。
- 双防线设计：分布式锁（TTL > 任务最大时长）挡并发，数据库唯一键（task+batch_date）挡 TTL 过期后的迟到重复；幂等是兜底不是唯一防线。
- "skipped-duplicate" 不重试只记录；观测按 task_id+参数聚合短窗口重复执行告警，业务指标异常（报表翻倍）是滞后信号。

## 复盘追问
- 为什么滚动更新期间的"短暂双 beat"也会出事故？提示：crontab 条目若恰在更新窗口触发，新旧 beat 各投一次，单次双跑就足以让账务任务重复入账——更新策略用 Recreate 或错开触发时间。
- 事故后"给任务加锁"就够了吗？提示：不够——锁的实现本身有失效模式（TTL、时钟、Redis 故障），必须问"锁失效时第二道防线是什么"，答案应是幂等键/登记表而不是"再加一把锁"。
