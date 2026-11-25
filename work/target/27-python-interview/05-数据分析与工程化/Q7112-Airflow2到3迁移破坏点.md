---
title: [Q7112] Airflow 2 到 3 的迁移破坏点
date: 2026-11-21
categories: [Python数据分析与工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7112 · Airflow 2 到 3 的迁移破坏点与灰度路线

难度：P6 ｜ 标签：版本演进 / Airflow 3 / 调度

**问**：数据团队有 300+ 个 DAG 跑在 Airflow 2.9 上，计划迁 Airflow 3。除了升 Python 版本，真正的破坏点在哪？怎么设计灰度路线避免"升级日全队停摆"？

**答**：
- **结论**：Airflow 3（2025 GA）的破坏点分四类：① **DAG 定义面**——`execution_date` 语义改为 `logical_date`（2.x 已铺垫，3.x 移除旧别名与很多 `airflow.models` 私有 API），TaskFlow API 成为主推，老式 `PythonOperator` 依赖的 import 路径清理（`airflow.operators.python` → 统一入口）；② **执行面**——Task Execution Interface 重构（task SDK），Airflow 2 自定义 Operator/Plugin 依赖内部类的直接失效，这是最大工作量；③ **运行时面**——内置 scheduler HA 变化、DAG 版本化（同一 DAG 多版本并存）、DagBag 解析行为变化（top-level 代码更严格）、`AIRFLOW_HOME`/配置项改名一批；④ **周边面**——REST API v2（端点变化）、CLI 子命令重组（`airflow dags test` → `airflow dags test` 语义变化）、日志存储接口。真正的迁移成本通常不在 DAG 文件本身（官方升级工具能自动改大半），而在**自定义 plugin/sensor/回填脚本对私有 API 的依赖**。
- **取舍**：灰度路线：① **静态盘点先行**：用官方 `airflow upgrade check`（迁移工具）扫全部 DAG+plugin，输出破坏点清单按工作量分类；② 双环境并行：Airflow 2 与 3 各一套环境，**同一份 DAG 仓库**、同一元数据库只读复制，2 跑生产、3 跑影子调度（只记录不触发动作）；③ 分层灰度：先纯 TaskFlow 的简单 DAG → 普通 PythonOperator DAG → 自定义 plugin 重的 DAG，每层观察解析时长、调度延迟、任务成功率；④ 回填/依赖外部脚本（回补工具、监控查询）单独改造与验证；⑤ cutover 用"周末低峰 + 冻结 DAG 变更 + 一键切流"剧本，元数据库迁移工具一次到位，回滚靠保留 2 环境热备。
- **实战**：落地清单：① 每个团队指派 DAG owner 分片认领破坏点清单；② CI 增加"Airflow 3 兼容"测试 job：DAG import 无错 + 任务实例 dry-run；③ 影子调度对比两侧的调度时间戳差异（DST/时区语义变化重点验证，见 Q7093）；④ 私有 API 依赖改造方向：sensor/插件改用公开 TaskFlow 与 ObjectStore 接口，禁止再 import `airflow.models` 内部类；⑤ 升级窗口留两周双跑观察期，指标：DAG 解析耗时、调度延迟 P95、失败率环比。

```python
# DAG 兼容性静态盘点 + 分层灰度调度（标准库模拟）
# 基线：Python 3.9+；真实工具 airflow-upgrade-check + 影子调度环境

import ast
import re
from dataclasses import dataclass


PRIVATE_API_RE = re.compile(r"from\s+airflow\.models(\.\w+)?\s+import|airflow\.operators\.python")
RISKY_CALLS = {"execution_date", "run_id=True", "get_dagrun"}


@dataclass
class DagInfo:
    name: str
    source: str
    uses_taskflow: bool


def scan_dag(d: DagInfo) -> list[str]:
    findings = []
    if PRIVATE_API_RE.search(d.source):
        findings.append("私有 API import（models/operators.python）")
    for c in RISKY_CALLS:
        if c in d.source:
            findings.append(f"旧语义调用: {c}")
    if not d.uses_taskflow:
        findings.append("非 TaskFlow 风格（建议迁移）")
    return findings


def grey_plan(dags: list[DagInfo]) -> dict[str, str]:
    plan = {}
    for d in dags:
        issues = scan_dag(d)
        if any("私有 API" in i for i in issues):
            plan[d.name] = "第3批(改造 plugin 后迁)"
        elif d.uses_taskflow and not issues:
            plan[d.name] = "第1批(纯TaskFlow直接迁)"
        else:
            plan[d.name] = "第2批(改写后迁)"
    return plan


def main() -> None:
    dags = [
        DagInfo("daily_report", "from airflow.operators.python import PythonOperator; x = get_dagrun(1)", False),
        DagInfo("ml_train", "@dag def f(): ...", True),
        DagInfo("etl_chain", "@dag\ndef f(): ...\nfrom airflow.models.baseoperator import BaseOperator", True),
    ]
    plan = grey_plan(dags)
    assert plan["ml_train"] == "第1批(纯TaskFlow直接迁)"
    assert plan["daily_report"] == "第3批(改造 plugin 后迁)"
    assert plan["etl_chain"] == "第3批(改造 plugin 后迁)"   # 私有 import 优先级最高
    assert scan_dag(dags[0]) != []
    print("OK: 静态盘点分三批灰度，私有 API 依赖是最大工作量项")
    for k, v in plan.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
```

**追问 1**：为什么影子调度比"测试环境手动触发"更能暴露迁移问题？
→ 一句话提示：影子调度用真实 DAG 全量、真实调度节奏跑"只记录不执行"，能暴露解析耗时膨胀、调度延迟、依赖判断错误这类只有持续运行才出现的问题；手动触发只验证单点。

**追问 2**：DAG 版本化（3.x 新特性）对回填有什么改变？
→ 一句话提示：回填时可以指定 DAG 代码版本，"用当时的代码回补当时的数据"，消除"代码已改、历史补数用新逻辑"的口径漂移；代价是要理解版本切换与 serialized DAG 的对应关系。

## 背诵要点
- Airflow 3 迁移最大工作量是自定义 plugin/sensor 对私有 API（airflow.models、operators.python 路径）的依赖，官方升级工具只能自动改 DAG 文件的大半。
- 灰度三步：升级工具静态盘点分批 → 双环境影子调度（只记录不执行）→ 分层 cutover（纯 TaskFlow → 改写 DAG → plugin 重的），回滚靠 2 环境热备。
- 升级日冻结 DAG 变更，观察指标：解析耗时、调度延迟 P95、失败率环比；时区/DST 语义单独验证。

## 复盘追问
- 为什么很多团队迁移后才发现"回补脚本"坏了？提示：回填/监控脚本直接查元数据库表或调 v1 REST API，属于 DAG 仓库之外的隐性依赖；盘点范围必须包含"绕过 Airflow 接口直接操作 Airflow 的工具"。
- TaskFlow API 迁移除了语法还有什么实质收益？提示：参数类型化（XCom 序列化可控）、任务间依赖由函数签名推导减少人为漏依赖、partial/expand 的动态映射原生支持——是重构成"可测试 DAG"的机会而不仅是兼容改造。
