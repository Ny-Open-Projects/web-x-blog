---
title: "[Q7705] MCP annotations 工具意图与权限提示的边界"
date: 2026-11-23
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7705 · MCP annotations 工具意图与权限提示的边界

难度：P7 ｜ 标签：原理取舍、MCP、工具权限、安全提示

基线：Python 3.12；MCP 2024-11 / 2025 规范的 `annotations` 字段；纯 Python 提示合并演示。

**问**：MCP 工具定义里有个 `annotations` 字段（`readOnlyHint`、`destructiveHint`、`idempotentHint`、`openWorldHint`）。有人说"用它做权限控制，声明只读的工具就给只读权限"。这个理解对吗？它到底该用来做什么？

**答**：
- **结论**：这是个常见误解。`annotations` 是**给客户端/模型的提示（hint）**，不是安全约束——服务端声明 `readOnlyHint: true` 只是"我承诺这个工具不改状态"，服务端完全可以在实现里偷偷写库，MCP 协议不会强制。它的正需要用处是：(1) 客户端 UI 据此展示风险提示、决定要不要弹确认；(2) Agent 据此做初步的工具选择/风险分级；(3) `idempotentHint` 帮客户端决定是否可安全重试。真正的安全边界必须在**服务端权限系统**和宿主侧的工具白名单/沙箱里实现，不能信 hint。
- **取舍**：把 hint 当软提示能提升 UX 和自动化程度，但若当成硬授权就会出越权事故——恶意或被攻陷的 MCP server 可谎报只读。反过来，完全忽略 hint 又放弃了有用的自动化信号。正确姿势是"hint 用于提示与排序，权限用独立机制兜底，且对 hint 做一致性观测（声明只读却产生写操作的工具要告警）"。
- **实战**：接入第三方 MCP server 时，按最小权限配宿主白名单，不因 `readOnlyHint` 放松；对 `destructiveHint=true` 的工具强制 human-in-the-loop 确认；记录工具实际副作用与声明 hint 的偏差，纳入审计。

```python
def risk_level(annotations: dict) -> str:
    """根据 hint 给出交互风险等级（仅提示，不作授权依据）。"""
    if annotations.get("destructiveHint"):
        return "high: 需人工确认"
    if not annotations.get("readOnlyHint", False):
        return "medium: 可能写状态"
    return "low: 声明只读（仍需服务端权限兜底）"


if __name__ == "__main__":
    for ann in (
        {"readOnlyHint": True},
        {"readOnlyHint": False, "idempotentHint": True},
        {"destructiveHint": True},
    ):
        print(risk_level(ann))
    # hint 只决定交互提示；授权必须由宿主白名单/服务端权限独立保证。
```

**追问一**：`idempotentHint` 为什么对重试策略有用？
→ 解析：幂等工具重复调用不产生额外副作用，客户端超时后可安全重试；非幂等工具重试可能造成重复下单、重复扣款，需要幂等键或禁止自动重试。hint 帮客户端决定重试策略，但仍需服务端真正实现幂等。

**追问二**：如何防止 MCP server 谎报 `readOnlyHint`？
→ 解析：协议层无法防止，必须靠宿主的最小权限白名单（数据库账号只读、文件系统只读挂载）和运行时副作用审计。对"声明只读却出现写操作"的工具做告警并下线。
