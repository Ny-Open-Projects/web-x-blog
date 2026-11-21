---
title: "[AD-063] 上下文·tool_call_id（关联）"
date: 2026-11-18
categories: [Java面试, Agent开发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 上下文 · tool_call_id（关联）

- **事实**：工具结果消息通过 tool_call_id 与调用请求关联（一次调用对应一条结果），多工具并行时靠 id 匹配
- **原理**：并行调用（AD-008）的结果必须按 id 回填（错位=结果张冠李戴），id 关联是并行正确性的协议保证
- **常见误区**：
  1. 结果按顺序回填即可（错）
  2. tool_call_id 是可选装饰（错）
  3. 并行结果顺序天然正确（错）
- **工程用法**：并行回填协议
- **版本锚点**：实战共识
