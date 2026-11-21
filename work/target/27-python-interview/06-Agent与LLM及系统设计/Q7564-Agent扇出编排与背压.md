---
title: [Q7564] Agent 扇出/扇入编排与背压
date: 2026-11-20
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7564 · Agent 扇出/扇入编排与背压

难度：P7 | 标签：Agent 编排、并发控制、部分失败、背压

**问**：一个主 Agent 要并发派出 20 个子 Agent 分别调研再汇总。扇出/扇入编排要处理哪些工程问题？"部分失败"的结果怎么聚合回上下文？

**答**：
- **结论**：四件事：① 并发上限——子 Agent 每个都是真金白银的 token 消耗，扇出必须设全局并发池上限（同时受供应商配额约束），否则一次任务烧掉一天的预算；② 单分支超时——每个子 Agent 独立超时，一个卡死的分支不能拖住整体 fan-in；③ 失败聚合——失败的分支把"失败原因"作为信息写回上下文（主 Agent 可以补派或绕过），而不是让整个任务抛异常；④ 结果结构化——fan-in 的汇总输入要做裁剪（每分支只回流结论+引用，不回流全程对话），否则上下文瞬间爆炸。
- **取舍**：同步 fan-out（简单、整体延迟=最慢分支）vs 流式 fan-in（先完成的先进上下文，主 Agent 可提前决策，但复杂）；取消传播：主 Agent 决定提前终止时，要显式取消所有在途子任务（asyncio TaskGroup / future.cancel），否则子任务在后台继续烧钱——"任务取消了但钱还在扣"是扇出编排最典型的成本事故。
- **实战**：背压设计：子任务队列深度超过阈值时主 Agent 先做"收敛"（合并相似子任务）再派发；每个分支带预算上限（最大步数、最大 token），分支级熔断进编排器统一记账。监控按"任务→分支"两级看成本，扇出任务的 P95 成本远高于均值说明存在分支失控。

```python
"""Agent 扇出编排：并发上限 + 单分支超时 + 部分失败聚合。"""
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def branch(name, seconds):
    time.sleep(seconds)
    if name == "b3":
        raise RuntimeError("上游 500")
    return f"{name}-done"

def fan_out(branches, max_workers=3, per_branch_timeout=2.0):
    results, failed = {}, []
    with ThreadPoolExecutor(max_workers=max_workers) as ex:   # 并发上限=池大小
        futs = {ex.submit(branch, n, s): n for n, s in branches}
        for f in as_completed(futs, timeout=per_branch_timeout * 3):
            n = futs[f]
            try:
                results[n] = f.result(timeout=per_branch_timeout)
            except Exception as e:
                failed.append((n, repr(e)))      # 单分支失败聚合，不中断整体
    return results, failed

results, failed = fan_out([("b1", 0.1), ("b2", 0.3), ("b3", 0.2)])
print("成功:", results, "失败:", failed)
print("要点：扇出要有并发上限（配额/费用）、单分支超时、失败聚合回上下文而非中断")
```

**追问链**：
1. 追问一层：为什么 fan-in 的输入要"裁剪回流"而不把子任务全程对话给主 Agent？——20 个分支的完整对话轻松超过上下文窗口，且噪声降低汇总质量；子 Agent 先自我总结成"结论+引用+置信度"再回流。
2. 追问二层：asyncio 下取消传播怎么做才彻底？（TaskGroup 退出时自动取消子任务并等待结束；子任务内部要把 CancelledError 转换为清理+上抛，不能吞掉）

**背诵要点**：
1. 扇出必须有并发上限与分支预算，否则一次任务烧光配额。
2. 失败分支聚合为信息回上下文；汇总输入只回流结论+引用。
3. 主任务终止必须传播取消，防"任务停了钱还在扣"。

**复盘追问**：
1. 扇出任务成本 P95 是均值 5 倍，怎么定位失控分支？（分支级 token 记账 + 步数分布）
2. 一个分支卡死把整体延迟拖到超时，为什么单分支超时没生效？（超时只包了 future.result 没覆盖排队时间，或子任务吞了取消）
