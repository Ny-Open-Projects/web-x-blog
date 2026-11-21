---
title: "[AD-197] 手写·mock（测试）"
date: 2026-11-18
categories: [Java面试, Agent开发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 手写 · mock（测试）

- **事实**：mock 模型实现：ModelClient 的测试实现（按剧本返回预设响应序列），剧本驱动（AD-039），mock 也要模拟 token 计数（预算路径测试）
- **原理**：mock 模型的实现要点（剧本序列化/usage 模拟/错误注入），mock 保真（AD-169）与可控平衡，与测试代码实践联动
- **常见误区**：
  1. mock 返回 null 即可（错）
  2. mock 不模拟 usage（错）
  3. 剧本无需存储（错）
- **工程用法**：mock 模型实现
- **版本锚点**：实战共识
