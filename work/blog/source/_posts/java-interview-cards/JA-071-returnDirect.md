---
title: "[JA-071] Spring AI·returnDirect（工具）"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## Spring AI · returnDirect（工具）

- **事实**：@Tool(returnDirect=true) 让工具结果直接返回用户不再回模型
- **原理**：适合最终答案型工具（查询类直接出结果），省一轮模型调用降低延迟与成本
- **常见误区**：
  1. returnDirect 是默认行为（错）
  2. 直接返回会绕过模型格式化（错）
  3. 所有工具都该 returnDirect（错）
- **工程用法**：低延迟查询工具优化
- **版本锚点**：Spring AI 1.0 GA
