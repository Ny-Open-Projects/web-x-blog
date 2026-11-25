---
title: "[Q7206] Airflow catchup：上线当天补跑两年任务"
date: 2026-11-23
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7206 · Airflow catchup：上线当天补跑两年任务

难度：P6 ｜ 标签：Airflow、catchup、回填、调度

基线：Python 3.12；Airflow 2.x `catchup` 语义；纯 Python 模拟调度窗口。

**问**：一个新 DAG 的 `start_date` 写成了两年前，`schedule="0 2 * * *"`，没显式设 `catchup`。上线后调度器瞬间创建了 700 多个 DagRun，数据库连接被打满，下游报表库被重复写入。`catchup` 默认是什么？为什么"补历史"会变成事故？

**答**：
- **结论**：Airflow 的 `catchup` 默认是 **True**：调度器会从 `start_date` 到当前时间，为每个未执行的调度区间创建 DagRun。`start_date` 写得太早 + 默认 catchup，就会一次性补跑几百上千个周期。每个 run 都打下游，资源被瞬间放大；如果任务不幂等，还会重复写数据。
- **取舍**：`catchup=False` 只跑当前/最近一个区间，适合"只看最新"的报表；需要补历史时用显式 `airflow dags backfill --start-date --end-date`，可控范围、限并发、分批执行。catchup=True 适合"每个周期都必须算"的场景，但要配 `max_active_runs`、池配额和幂等写入。
- **实战**：① `start_date` 用固定历史点（不要用 `datetime.now()`，否则每次解析都变）；② 新 DAG 默认 `catchup=False`，补历史走显式 backfill；③ 任务必须幂等（按分区覆盖/merge），否则重跑就重复；④ 限制 `max_active_runs` 与 pool slot，避免回填挤占实时任务；⑤ 回填前评估下游库的连接数与写入能力。

```python
import datetime as dt


def dag_runs(
    start: dt.date, deploy: dt.date, catchup: bool, backfill_days: int | None = None
) -> dict[str, int]:
    if catchup:
        n = (deploy - start).days
        mode = "catchup"
    elif backfill_days:
        n = backfill_days
        mode = "explicit_backfill"
    else:
        n = 1
        mode = "latest_only"
    return {"runs": n, "mode": mode}


if __name__ == "__main__":
    start = dt.date(2024, 11, 23)
    deploy = dt.date(2026, 11, 23)
    for catchup, days in ((True, None), (False, None), (False, 30)):
        r = dag_runs(start, deploy, catchup, days)
        print(f"{r['mode']:>16}: {r['runs']} 个 run, "
              f"按 2 分钟/run 约 {r['runs'] * 2 / 60:.0f} 小时")
    print("结论：start_date 过早 + 默认 catchup 会把两年历史一次性补跑")
```

**追问一**：`catchup=False` 之后还能补历史吗？
→ 解析：能，用 `airflow dags backfill` 显式指定起止日期，或手动 `trigger_dag` 带 logical date。catchup 只控制"调度器是否自动补齐错过的区间"，不取消回填能力；显式回填更可控，能限并发、分批、先跑一个月验证。

**追问二**：为什么回填任务必须幂等，光靠 catchup 不够？
→ 解析：回填会把同一逻辑日期重跑多次（失败重试、人工重跑、补数），如果任务是 append 写入，每次都会重复追加；必须按 `logical_date`/分区做覆盖或 merge，保证"同一区间跑 N 次结果一致"。幂等是回填的前提，不是可选项。
