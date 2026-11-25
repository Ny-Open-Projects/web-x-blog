---
title: [Q7654] 工具定义 token 占用与按需装载容量账
date: 2026-11-21
categories: [PythonAgent与系统设计]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7654 · 工具定义 token 占用与按需装载容量账

难度：P6-P7 | 标签：MCP、上下文预算、容量规划

**问**：接入 MCP 后注册了 60 个工具，每个工具 schema 约 300 token，每轮请求光工具定义就吃掉 1.8 万 token，长会话很快顶到上下文上限。工具定义的 token 账怎么算？按需装载怎么做？

**答**：结论：工具定义是**每轮都重复计费的固定开销**，成本 = 工具数 × 平均 schema token × 轮数；60 个工具常驻时，它可能超过对话本身的 token 量。治理按三级：① 精简 schema：参数描述压缩、删示例，单工具从 300 压到 120 token 通常无损；② 分组按需装载：按任务域分组（检索组/邮件组/代码组），运行时只挂当前域 5-8 个工具，用"工具路由器"（先分类再装组）；③ 动态发现：MCP 的 tools/list 按需拉取 + 关键词过滤，会话切域时换装。

实战要点：
1. 账目监控：每轮请求打点"工具定义 token / 总输入 token"，占比 >30% 即触发治理（Q7645 会话裁剪是另一维，两者叠加算总账）。
2. 装换装的成本：切组会丢上一组工具的"肌肉记忆"，把跨组高频工具（如时间、搜索）常驻，冷门组按需。
3. 与 prompt cache 协同：工具定义放最前缀且顺序稳定，服务端前缀缓存（Q7574）才能命中——动态乱序装载会把缓存打没，装载要"追加式"而非"重排式"。

```python
"""工具定义 token 账与分组按需装载（标准库，可运行）"""
from dataclasses import dataclass, field


@dataclass
class ToolGroup:
    name: str
    tools: list[str]
    tokens_per_tool: int = 120

    def cost(self) -> int:
        return len(self.tools) * self.tokens_per_tool


@dataclass
class ContextLedger:
    groups: dict[str, ToolGroup]
    resident: set[str] = field(default_factory=set)   # 常驻组
    active: set[str] = field(default_factory=set)     # 当前挂载组

    def tool_token_per_turn(self) -> int:
        groups = [self.groups[g] for g in (self.resident | self.active)]
        return sum(g.cost() for g in groups)

    def load(self, group: str, budget: int) -> str:
        """按需装载：超预算拒绝并提示裁剪"""
        self.active.add(group)
        used = self.tool_token_per_turn()
        if used > budget:
            self.active.discard(group)
            return f"reject: {used}>{budget}, 裁剪后再装"
        return f"loaded {group}, tool tokens={used}"


groups = {
    "search": ToolGroup("search", ["web", "kb", "time"]),
    "mail": ToolGroup("mail", ["send", "list", "read", "draft"]),
    "code": ToolGroup("code", ["run", "lint", "test", "diff"]),
}
led = ContextLedger(groups, resident={"search"})
print("常驻每轮:", led.tool_token_per_turn(), "token")
print(led.load("mail", budget=1000))
print(led.load("code", budget=1000))  # 6 工具常驻mail + 4 code 超预算
```

**追问 1**：为什么"把工具定义写在系统提示里"比结构化 tools 字段更不可控？
**提示**：无 schema 校验、模型容易漏参数或改字段名，且结构化 tools 才能吃到 API 层的前缀缓存与调用协议保障。

**追问 2**：分组路由器自己分类错了会怎样？
**提示**：装错组导致无可用工具，模型要么放弃要么幻觉编造调用；路由器要给低置信度回退（装载默认组+提示重分类）。

## 背诵要点
- 工具定义是每轮重复固定开销：工具数 × schema token × 轮数，占比 >30% 必须治理。
- 治理三级：精简 schema → 分组按需装载 → 动态发现；跨组高频工具常驻。
- 装载必须追加式保顺序稳定，否则打没服务端前缀缓存。

## 复盘追问
- 60 个工具里，最近 30 天实际被调用过的占比多少？瘦身清单怎么生成？
- 切域换装时如何避免丢上下文？（组间交接摘要？）
