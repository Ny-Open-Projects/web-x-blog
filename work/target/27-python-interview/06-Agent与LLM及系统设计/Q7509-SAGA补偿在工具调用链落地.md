---
title: [Q7509] SAGA 补偿在 LLM 工具调用链的落地
date: 2026-11-18
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7509 · SAGA 补偿在 LLM 工具调用链的落地(部分失败回滚)

> 难度:★★★ | 标签:Agent, 分布式一致性, 事务

**问**：Agent 执行"查航班→订酒店→租车→发确认邮件"的工具链，第 3 步失败了，前两步已产生真实订单。通用 SAGA 模式我知道，但工具是 LLM 动态决定的，补偿怎么落地？哪些工具根本没有补偿能力？

**答**：结论：SAGA 落到工具链的关键改造是**把补偿计划从"运行时由 LLM 决定"改为"注册时静态声明"**——每个工具注册时声明 `compensate`（补偿动作）、`compensable`（是否可补偿）、`pivot`（关键不可回滚点），编排层据此维护补偿栈。原则：**不可补偿的工具（发邮件、外呼、真实扣款）必须放在 pivot 之后**，pivot 之前只放可补偿工具；LLM 只负责填参数，不负责决定回滚——让模型临场"想出"补偿动作是事故温床。

落地与实战：
- 补偿栈的语义：每成功执行一个 compensable 工具就压栈（记录输入输出与幂等键），失败时按**逆序**弹栈补偿，补偿也要幂等（同一订单取消两次等价）且带重试；补偿失败不能静默，进人工干预队列（这是 SAGA 与 2PC 的本质区别：允许中间态，靠补偿收敛）。
- 与 LLM 的边界：模型输出工具调用 → 编排层校验"该工具在当前阶段是否允许"（pivot 前禁不可补偿工具）→ 执行 → 成功压栈。若模型非要先发邮件再订酒店，编排层拒绝并提示重排——权限与顺序治理在代码里，不在提示词里。
- 事故复盘：某 Agent 先发确认短信再扣款，扣款失败短信已出，客诉。修复：工具注册表标注 `non_compensable`，编排器把"通知类"工具强制排到事务收尾（pivot 后），并在轨迹里记录补偿计划（哪些步骤会回滚），失败时用户看到的错误信息明确"订单已取消，无任何扣款"。补偿计划透明化把投诉率降了一个量级。

```python
# 基线:Python 3.9+ 标准库;SAGA 编排器:补偿栈 + pivot 闸门(可运行)
from dataclasses import dataclass, field
from typing import Callable

@dataclass
class Tool:
    name: str
    run: Callable[[dict], str]
    compensate: Callable[[dict], str] | None   # None = 不可补偿
    idempotency: str = ""

@dataclass
class SagaOrchestrator:
    stack: list[tuple[Tool, dict]] = field(default_factory=list)
    def execute(self, tool: Tool, args: dict) -> str:
        if tool.compensate is None and self.stack:   # pivot 闸门:已有可补偿步骤后禁不可回滚
            pass  # 实际策略:不可补偿工具应在流程收尾;此处演示记录
        result = tool.run(args)
        if tool.compensate is not None:
            self.stack.append((tool, args))
        return result
    def rollback(self) -> list[str]:
        actions = []
        while self.stack:                            # 逆序补偿
            tool, args = self.stack.pop()
            actions.append(tool.compensate(args))    # 补偿需幂等,带原幂等键重试
        return actions

def book_hotel(args: dict) -> str:
    return f"booked:{args['id']}"                    # 真实实现:调外部 API

def cancel_hotel(args: dict) -> str:
    return f"cancelled:{args['id']}"                 # 幂等:重复取消等价

if __name__ == "__main__":
    saga = SagaOrchestrator()
    hotel = Tool("book_hotel", book_hotel, cancel_hotel, idempotency="bk-1")
    print(saga.execute(hotel, {"id": "bk-1"}))
    print("补偿:", saga.rollback())                   # 模拟后续步骤失败
```

**追问**：
- 一层追问：补偿动作本身失败了怎么办？——升级路径：自动重试（幂等前提）→ 延迟重试队列 → 人工干预工单，并把"补偿失败"作为独立告警级别（比原失败更严重，因为系统进入不一致态）；这要求补偿操作有查询接口（查该订单到底取消没有）而不是盲发指令。
- 二层追问：LLM 在 SAGA 里到底该承担什么？——参数填充与异常解释，不承担控制流。控制流（顺序、补偿、pivot）由编排器静态保证；若业务确需模型动态规划流程，也要在规划输出后先经静态校验（DAG 校验器）再执行，即"计划-验证-执行"三段式。
- 三层追问：怎么测试补偿链路？——故障注入：在每一步后注入失败，断言"外部系统终态 = 全部回滚"；补偿幂等测试（同一补偿跑两次）；以及混沌场景（补偿 API 超时）。工具链的 SAGA 测试重点是外部依赖的终态对账，不是代码覆盖率。
