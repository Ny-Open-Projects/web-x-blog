---
title: [Q7502] ReAct 循环的步数预算推导与熔断恢复设计
date: 2026-11-18
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7502 · ReAct 循环的步数预算与死循环熔断恢复设计

> 难度:★★★ | 标签:Agent, ReAct, 可靠性

**问**：我们的 ReAct Agent 偶尔陷入"搜索-无结果-再搜索"循环烧钱，现在靠一个硬编码 max_steps=10 截断。步数预算应该怎么推导？熔断之后呢——直接报错、还是要有恢复策略？

**答**：结论：max_steps 不该拍脑袋，它是一个**成本-时延-成功率的三方预算**：按任务类型的历史轨迹分布（P50 步数、P95 步数）推导，预算取 P95 × 1.2，并按任务分级（简单查询 5 步、调研型 15 步、流水线型按 DAG 层数 × 扇出）。熔断不能只有"截断"一个动作，要按死循环的**类型**给恢复策略：重复相同工具+相同参数 → 立即熔断并降级（返回部分结果+说明）；连续无效但参数在变化 → 注入反思提示（reflection）给一次重预算；预算耗尽但已有中间产物 → 走"收尾模式"（让模型基于已有信息给出最佳答案并标注置信度）。

推导与实战：
- 预算还含经济维度：单步成本 ≈ 输入 token（随历史线性涨）+ 工具调用费；步数预算乘以单步成本 = 单任务成本上限，这个上限要进网关配额，而不是等账单教做人。
- 熔断判据分层：硬熔断（步数/时间/token 超限，确定性）+ 软熔断（检测重复：对"工具+参数哈希"做签名去重，同一签名第 2 次警告、第 3 次熔断；观测停滞：连续 N 步任务状态无变化）。熔断本身要幂等且记录熔断原因到轨迹，供离线归因。
- 事故复盘：某 Agent 因搜索工具返回空列表，模型以"再搜一次换个词"循环 40 步，烧掉 30 美元。修复：签名去重（10 秒内同参调用直接熔断）+ 空结果注入提示"连续两次无结果请改用其他工具或收尾"，同类事故步数从 40 降到 3。

```python
# 基线:Python 3.9+ 标准库;步数预算推导 + 分级熔断状态机(可运行)
import hashlib, json

def derive_budget(percentiles: dict[str, float], headroom: float = 1.2) -> int:
    """按历史轨迹 P95 × 1.2 推导步数预算。percentiles 如 {"p50":3,"p95":12}"""
    return int(percentiles["p95"] * headroom)

def call_signature(step: dict) -> str:
    """工具+参数签名,死循环检测的基本单元。"""
    payload = json.dumps({"tool": step["tool"], "args": step["args"]}, sort_keys=True)
    return hashlib.sha256(payload.encode()).hexdigest()

class LoopGuard:
    """软熔断:同签名第 2 次警告、第 3 次熔断。"""
    def __init__(self) -> None:
        self.seen: dict[str, int] = {}
    def check(self, step: dict) -> str:
        sig = call_signature(step)
        n = self.seen.get(sig, 0) + 1
        self.seen[sig] = n
        if n >= 3:
            return "CIRCUIT_BREAK"      # 立即熔断,降级收尾
        if n == 2:
            return "WARN"               # 注入反思提示
        return "OK"

if __name__ == "__main__":
    print("预算:", derive_budget({"p50": 3, "p95": 12}))
    g = LoopGuard()
    step = {"tool": "search", "args": {"q": "x"}}
    for _ in range(3):
        print(g.check(step))
```

**追问**：
- 一层追问：步数预算耗尽就失败，用户体感差，怎么平衡？——分层预算：总预算内先走主线；触达 80% 时给模型提示"剩余预算"，模型自行收敛；耗尽走收尾模式输出部分结果。评估指标要加"预算内完成率"与"收尾质量"，而不是只有成功率。
- 二层追问：反思提示（reflection）会不会引入新循环？——会：模型反思后可能原路重来。工程约束：反思次数上限（1 次）+ 反思提示必须携带结构化失败原因（空结果/权限不足/超时），让下一轮行为可验证地改变，否则同样签名熔断。
- 三层追问：步数预算和 token 预算谁说了算？——双闸门取先到者：步数控制行为复杂度，token 控制成本；步数相同任务 token 可差 10 倍（长输出工具），所以成本敏感场景以 token 预算为主、步数为辅助熔断。
