---
title: [Q349] 调度系统 Airflow 概念与任务编排
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q349 · 调度系统 Airflow 概念与任务编排

> 难度:★★★ | 标签:Airflow, 调度

**问**:Airflow 的核心概念有哪些?设计 DAG 时要注意什么?

**答**:核心概念:DAG(工作流)、Task(节点)、Operator(任务类型)、依赖关系(`>>`)、schedule 与数据间隔、execution_date/逻辑日期。设计要点:①任务粒度适中,一个 task 一个职责,失败可单独重跑;②依赖显式声明,避免用 sleep 凑时序;③任务保持幂等,重跑安全是调度的前提;④execution_date 是"数据日期"而非运行时间,回填 backfill 依赖这一点;⑤避免在 DAG 文件里做重计算,DAG 定义要秒级解析。这些原则同样适用于其他调度器(DolphinScheduler、Argo)。

```python
# file: code/05_数据分析与工程化/q349_scheduler_dag.py
"""概念级 DAG 演示:用标准库表达 依赖 + 幂等任务 + 逻辑日期,
生产上对应 Airflow 的 DAG 定义。"""
from dataclasses import dataclass, field

@dataclass
class Task:
    task_id: str
    fn: callable
    upstream: list = field(default_factory=list)

class Dag:
    def __init__(self, dag_id, execution_date):
        self.dag_id = dag_id
        self.execution_date = execution_date   # 逻辑日期,即数据日期
        self.tasks = {}

    def add(self, task):
        self.tasks[task.task_id] = task
        return self

    def run(self):
        done = {}
        def visit(tid):
            if tid in done:
                return done[tid]
            t = self.tasks[tid]
            for up in t.upstream:              # 依赖先行
                visit(up)
            done[tid] = t.fn(self.execution_date)
            return done[tid]
        for tid in self.tasks:
            visit(tid)
        return done

def extract(date): return f"raw@{date}"
def transform(date): return f"clean@{date}"
def load(date): return f"loaded@{date}"

if __name__ == "__main__":
    dag = Dag("user_etl", "2026-11-01")
    dag.add(Task("extract", extract))
    dag.add(Task("transform", transform, ["extract"]))
    dag.add(Task("load", load, ["transform"]))
    print(dag.run())
```

**追问**:
- execution_date 为什么容易理解错?——它是数据日期(区间左端)不是运行时间;每日任务在次日跑,execution_date 是前一天,回填逻辑全靠它。
- 怎么避免用 sleep 凑时序?——显式声明依赖 `upstream >> downstream`;外部系统就绪用 sensor 而不是猜时间。
- DAG 文件为什么要秒级解析?——调度器周期性解析所有 DAG 文件,文件里的重计算会拖垮调度循环;重活放 task 内。

---
