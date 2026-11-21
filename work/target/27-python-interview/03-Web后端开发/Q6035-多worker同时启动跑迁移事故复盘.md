---
title: [Q6035] 多 worker 同时启动跑迁移的事故复盘
date: 2026-11-20
categories: [PythonWeb后端]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q6035 · 多 worker 同时启动跑迁移：启动竞态事故复盘

> 难度:★★★★ | 标签:事故复盘, 迁移, 启动竞态, Django

**问**：K8s 里 8 个 worker 同时启动，每个都在 startup 钩子里跑 `migrate`——会发生什么？为什么多数时候"看起来没事"？正确的迁移执行形态是什么？

**答**：事故形态取决于迁移的幂等性：Django 的 `django_migrations` 表让重复 migrate 大多"静默跳过"，所以平时没炸；但两个进程**同时**判断"迁移未应用"并各自执行同一 DDL 时，竞态开始——轻则 duplicate column 报错、重则锁等待把连接池打满（DDL 锁表，Q806 大表迁移的在线性问题）、还可能一个进程看到半完成的 schema。三层修复：1) **职责分离（治本）**：迁移是部署动作不是启动动作——Job/initContainer 专跑 migrate，跑完才放 Deployment 起应用；SaaS 多实例共享 DB 时迁移必须**单执行者**；2) **应用侧守门**：startup 只做"schema 版本断言"（读到预期版本号，不满足就快速失败退出让探针接管），把"启动即迁移"改成"启动即验证"；3) **迁移自身加锁兜底**：应用级 advisory lock（PG `pg_advisory_lock`）包住 migrate，即使双跑也只有一方执行——这是框架能力之外的保险（Django 无内置全局锁，Flyway/Liquibase 有，这就是"迁移工具要有锁"的选型理由）。关联：迁移与代码发布的两阶段兼容（Q816/Q6017）解决"旧代码+新 schema"，本卡解决"新代码执行迁移的竞态"，两者共同构成零停机发布的迁移面。

```python
# file: code/03_Web后端开发/q6035_migrate_race.py
"""迁移竞态三防御: 单执行者 / 启动即验证 / advisory lock 兜底."""
import random
import threading
import time

# --- 模拟: 8 个 worker 同时 startup, 各自想跑迁移 ---
SCHEMA = {"version": 0, "ddl_log": []}
LOCK = threading.Lock()                     # 充当 PG advisory lock 的替身

def run_migration_locked(worker: str, target_version: int) -> str:
    """advisory lock 兜底: 只有拿到锁的一方真正执行."""
    with LOCK:                              # pg: SELECT pg_advisory_lock(key)
        time.sleep(random.uniform(0, 0.01))  # 模拟 DDL 耗时
        if SCHEMA["version"] >= target_version:
            return f"{worker}: skip (already v{SCHEMA['version']})"
        SCHEMA["version"] = target_version
        SCHEMA["ddl_log"].append(f"{worker}->v{target_version}")
        return f"{worker}: applied v{target_version}"

def naive_migrate(worker: str, target_version: int) -> str:
    """反面教材: 无锁检查后执行, 检查与执行之间有窗口."""
    if SCHEMA["version"] < target_version:  # check
        time.sleep(random.uniform(0, 0.02))  # check 与 apply 之间的竞态窗口
        SCHEMA["version"] = target_version   # apply(双方都执行 -> DDL 冲突)
        SCHEMA["ddl_log"].append(f"{worker}(race)->v{target_version}")
        return f"{worker}: applied (race)"
    return f"{worker}: skip"

def startup_assert(expected: int) -> str:
    """正确的 startup 形态: 验证版本, 不满足就快速失败."""
    if SCHEMA["version"] < expected:
        raise SystemExit(f"schema v{SCHEMA['version']} < expected v{expected}; "
                         "等待 migrate Job 完成")
    return "schema OK, starting workers"

if __name__ == "__main__":
    import multiprocessing as mp

    def worker_entry(q, fn):
        q.put(fn(f"w{os.getpid()}", 1))

    import os

    # 竞态复现: 无锁双跑
    SCHEMA["version"] = 0
    ctx = mp.get_context("spawn")
    q = ctx.Queue()
    procs = [ctx.Process(target=worker_entry, args=(q, naive_migrate)) for _ in range(4)]
    for p in procs:
        p.start()
    for p in procs:
        p.join(timeout=5)
    logs = []
    while not q.empty():
        logs.append(q.get())
    print("无锁双跑结果:", logs)
    print("(真实 DB 场景: 双方都执行 DDL -> duplicate column / 锁等待)")

    # 兜底复现: advisory lock 串行化
    SCHEMA["version"] = 0; SCHEMA["ddl_log"] = []
    q2 = ctx.Queue()
    procs2 = [ctx.Process(target=worker_entry, args=(q2, run_migration_locked))
              for _ in range(4)]
    for p in procs2:
        p.start()
    for p in procs2:
        p.join(timeout=5)
    logs2 = []
    while not q2.empty():
        logs2.append(q2.get())
    print("advisory lock 结果:", logs2)
    print("正确部署形态: migrate 在独立 Job 单执行者跑完 -> 应用 startup 只断言版本")
```

**追问**：1) 为什么 Django 重复 migrate "多数没事"还有必要修？——幂等表只防"先后重复"，不防"同时执行"；DDL 的 CREATE TABLE IF NOT EXISTS 类语句竞态静默，ADD COLUMN 类直接炸，事故是概率性的且只发生在扩容/重启风暴时。2) advisory lock 的 key 怎么设计？——用"项目+迁移链"的稳定哈希做 key，锁超时大于最长迁移时长，持锁方崩溃要能被超时释放；锁粒度是整条 migrate 而不是单个迁移（保证链序）。3) migrate Job 失败时应用该不该起来？——不该：startup 断言失败快速退出，readiness 拒绝流量，等人工或重试修复；"带病启动"会把半 schema 暴露给流量，事故更大。

## 背诵要点
- 迁移是部署动作不是启动动作：initContainer/Job 单执行者跑，应用 startup 只做版本断言。
- 幂等表防"先后重复"不防"同时执行"；advisory lock（pg_advisory_lock）是框架外的竞态兜底。
- migrate 失败 → 应用快速失败 + readiness 拒流，绝不带半 schema 接流量。

## 复盘追问
- 你们平台的"迁移执行者"是谁？如果答案里有"每个实例自己"，扩容风暴时的爆炸半径是什么？
- 半完成的 DDL（迁移中途断掉）由谁负责恢复？人工 runbook 还是迁移工具的自动续跑？
